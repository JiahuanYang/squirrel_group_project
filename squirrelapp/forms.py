
from django import forms
from django.forms import ModelForm

from .models import SquirrelDetails

class LatiForm(ModelForm):
    class Meta:
        model = SquirrelDetails
        fields = [
            'Latitude',
            'Longitude',
            'Shift',
            'Date',
            'Age',]

# LongiForm

# class LongiForm(forms.Form):
    
    
