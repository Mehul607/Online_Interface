from django import forms

from .models import Sentence

class sentenceForm(forms.ModelForm):
    class Meta:
        model=Sentence
        fields=['stext',]