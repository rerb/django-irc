from django.db.models import get_model

from aashe.organization.models import Organization

class LoaderException(Exception):
    pass


class BaseLoader(object):
    def __init__(self, parser_class, model_or_string, reset=False, **kwargs):
        '''
        Setup the loader with the parser_class to use and the model
        to dump the parser's data into. The model can be specified
        as an actual models.Model subclass or as a string that
        specifies the model in Django's `app.model` syntax.
        '''
        self.parser_class = parser_class
        self.parser = self.parser_class()
        self.reset = reset
        if isinstance(model_or_string, basestring):
            self.model = get_model(*model_or_string.split('.'))
        else:
            self.model = model_or_string
        if not self.model:
            raise ValueError("%s model_or_string kwarg must be valid Model subclass or Django app.Model string (%s)" % (self.__class__.__name__, self.parser_class.__name__))
        self.kwargs = kwargs

    def reset_model(self):
        self.model.objects.all().delete()

    def create_instance(self, data):
        raise NotImplemented


class GenericLoader(BaseLoader):
    '''
    Tries to match an organization to each resource, where
    data['institution'] ~= organization.name
    '''
    def match_institution(self, data):
        if data.has_key('institution'):
            try:
                inst_query = data['institution'].strip().lower()
                institution_obj = Organization.objects.get(
                    name__iexact=inst_query)
                data['organization'] = institution_obj
            except:
                note_line = "Institution is " + data['institution']
                try:
                    data['notes'] = '\n'.join((data['notes'], note_line))
                except KeyError:
                    data['notes'] = note_line
                del data['institution']

    def create_instance(self, data):
        init_args = {}
        self.match_institution(data)
        # iterate over all the keys in the dictionary provided by
        # the parser... any keys that are fields on the model, use
        # to construct a new instance of the model
        for key in data.keys():
            if key in self.model._meta.get_all_field_names() and data[key]:
                if type(data[key]) is str:
                    try:
                        data[key] = unicode(data[key])
                    except UnicodeDecodeError:
                        pass  # probably already utf-8 . . . right?
                init_args.update({key: data[key]})
        obj = self.model(**init_args)
        obj.save()
        return obj

    def load_all(self, reset=False):
        self.parser.parsePage()
        if self.reset:
            self.reset_model()
        for data in self.parser.data:
            try:
                self.create_instance(data)
            except:
                import sys, traceback
                exc_type, exc_value, exc_tb = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_tb)
                raise LoaderException('%s failed to load parser %s for %s' % (
                        self.__class__.__name__, self.parser_class.__name__,
                        self.model.__name__))
