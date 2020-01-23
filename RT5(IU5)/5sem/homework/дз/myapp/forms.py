from django import forms
from myapp.models import *


class UsForm(forms.ModelForm):
    class Meta:
        model = User2
        fields = ["name", "idconcert"]
        widgets = {'information': forms.Textarea(attrs={'resize': 'none'})}

class CoForm(forms.ModelForm):
    class Meta:
        model = Concert
        fields = ["name"]
        widgets = {'information': forms.Textarea(attrs={'resize': 'none'})}