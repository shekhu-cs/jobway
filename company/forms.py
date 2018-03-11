from django import forms
from .models import coforms


class Compform(forms.ModelForm):
    class Meta:
        model = coforms
        fields = ('name', 'website', 'role', 'description')

