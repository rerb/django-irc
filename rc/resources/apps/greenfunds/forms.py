from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.contenttypes.generic import generic_inlineformset_factory
from models import GreenFund, StudentFeeFund, DonationFund, DepartmentFund, HybridFund, FundTerm
from aashe.organization.models import Organization

class FundTermCreateForm(forms.ModelForm):

      class Meta:
          model = FundTerm

# TODO Make this work
# FundTermInlineForm = generic_inlineformset_factory(GreenFund, FundTerm, FundTermCreateForm, extra=1, can_delete=False)

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

class GreenFundUpdateForm(forms.ModelForm):
    
    class Meta:
        # model = RevolvingLoanFund
        exclude = ('object_id')
