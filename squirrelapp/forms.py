
from django import forms
from django.forms import ModelForm

from .models import SquirrelDetails

class LatiForm(ModelForm):
    class Meta:
        model = SquirrelDetails
        fields = [
            'Latitude',
        ]

# LongiForm

# class LongiForm(forms.Form):
    
    
