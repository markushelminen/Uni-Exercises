from django import forms
from django.forms.widgets import NumberInput
from models import Search

class searchForm(forms.ModelForm):
    
    class Meta:
        model = Search
        fields = ['user', 'service', 'radius']
        