from django import forms
from .models import Imeage

class ImeageFrom(forms.ModelForm):
    class Meta:
        model = Imeage
        fields = '__all__'
        labels = {'photot':''}