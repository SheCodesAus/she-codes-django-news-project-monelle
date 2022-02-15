from django import forms
from django.forms import ModelForm
from .models import NewsStory
import datetime


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content']
        widgets = {
            'pub_date': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class':'form-control',
                    'value':datetime.datetime.now().strftime('%Y-%m-%dT%H:%M')},
                format='%Y-%m-%dT%H:%M'),    
        }