from django import forms
from .models import Sightings

class SightingForm(forms.ModelForm):
    class Meta:
        model = Sightings
        fields = '__all__'
        help_texts = {'Date':('Enter the date of the sighting (YYYY-MM-DD)')}
