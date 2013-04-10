from django import forms
from django.contrib.contenttypes.generic import generic_inlineformset_factory
from django.forms.models import inlineformset_factory
from models import GreenFund, StudentFeeFund, DonationFund, DepartmentFund, HybridFund, FundTerm
from aashe.organization.models import Organization

# CRUD forms        
class GreenFundCreateForm(forms.ModelForm):

      class Meta:
          model = GreenFund
          exclude = ('published', 'notes')

GreenFundInlineForm = generic_inlineformset_factory(GreenFund, GreenFundCreateForm, extra=1, can_delete=False)

class FundTermCreateForm(forms.ModelForm):

      class Meta:
          model = FundTerm

FundTermInlineForm = inlineformset_factory(GreenFund, FundTerm, FundTermCreateForm, extra=1, can_delete=False)

class StudentFeeFundCreateForm(forms.ModelForm):
      
      class Meta:
          model = StudentFeeFund

class DonationFundCreateForm(forms.ModelForm):
      
      class Meta:
          model = DonationFund

class DepartmentFundCreateForm(forms.ModelForm):
      
      class Meta:
          model = DepartmentFund

class HybridFundCreateForm(forms.ModelForm):
      
      class Meta:
          model = HybridFund