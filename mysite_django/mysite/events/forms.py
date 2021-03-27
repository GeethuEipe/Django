from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Venue
from .models import Reg

  
class VenueForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Venue
        #venue = models.ForeignKey('venue')
        fields = '__all__'


class RegForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Reg
        fields = '__all__'