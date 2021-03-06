from base import ElectronicWasteParser, PageParser, SimpleTableParser


BASE_URL = 'http://www.aashe.org/resources/'


class ProgramTableParser(SimpleTableParser):

    url = None
    login_required = False

    def processTable(self, table, program_type, headings=True):
        programs = super(ProgramTableParser, self).processTable(
            table=table, headings=headings, save_resources=False)
        for program in programs:
            program['program_type'] = program_type
        self.data.extend(programs)


class BicycleSharePrograms(ProgramTableParser):
    '''
    >>> parser = BicycleSharePrograms()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'bicycle-share-programs'
    login_required = True

    def parsePage(self):
        tables = self.soup.findAll('table')
        # First 3 tables are 'Free Bicycle Share Programs'
        for table in tables[0:3]:
            super(BicycleSharePrograms, self).processTable(
                table, program_type='Free Bicycle Share Programs')
        # Last table is 'Bicycle Rental Programs'
        super(BicycleSharePrograms, self).processTable(
            tables[-1], program_type='Bicycle Rental Programs')


class CampusCompostingPrograms(ProgramTableParser):
    '''
    >>> parser = CampusComposting()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-composting-programs'
    login_required = True
    program_type = 'Campus Composting Program'

    def parsePage(self):
        table = self.soup.find('table')
        super(CampusCompostingPrograms, self).processTable(
                table, program_type=self.program_type)


class GreenOfficePrograms(ProgramTableParser):
    '''
    >>> parser = GreenOfficePrograms()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'green-office-programs'
    login_required = True
    program_type = 'Green Office'

    def parsePage(self):
        for table in self.soup.findAll('table'):
            super(GreenOfficePrograms, self).processTable(
                table, program_type=self.program_type)


class StudentSustainabilityEducatorPrograms(PageParser):
    '''
    >>> parser = StudentSustainabilityEducatorPrograms()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'peer-peer-sustainability-outreach-campaigns'
    login_required = True
    program_type = 'Student Sustainability Educator'

    def parsePage(self):
        content_div = self.soup.find('div', {'class': 'content clear-block'})
        for paragraph in content_div.findAll('p'):
            resource = {'program_type': 'Student Sustainability Educator'}
            try:
                institution = paragraph.find('strong').extract()
            except AttributeError:
                continue  # *probably* opening text
            resource['institution'] = institution.text
            anchor = paragraph.find('a').extract()
            resource['url'] = anchor['href']
            resource['title'] = anchor.text
            # anything left over is a note
            resource['notes'] = paragraph.text
            resource['program_type'] = self.program_type
            self.data.append(resource)


class SurplusPropertyRecyclingPrograms(ProgramTableParser):
    '''
    >>> parser = SurplusPropertyRecycling()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-surplus-recycling'
    login_required = True
    program_type = 'Surplus Property Recycling'

    def parsePage(self):
        for table in self.soup.findAll('table'):
            super(SurplusPropertyRecyclingPrograms, self).processTable(
                table, program_type=self.program_type)


class GreenCleaningPrograms(ProgramTableParser):
    '''
    >>> parser = GreenCleaningPrograms()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'green-cleaning'
    login_required = True
    program_type = 'Green Cleaning'

    def parsePage(self):
        # Programs are listed only in the first table on this page.
        programs_table = self.soup.find('table')
        super(GreenCleaningPrograms, self).processTable(
                table=programs_table, program_type=self.program_type)


class ElectronicWastePrograms(ElectronicWasteParser):

    program_type = 'Electronic Waste'

    def parsePage(self):
        super(ElectronicWastePrograms, self).parsePage('programs')
        for program in self.data:
            program['program_type'] = self.program_type
