from .models import kontakt, SnusProdut
from django.forms import ModelForm
from django import forms

class KontaktSender(forms.ModelForm):
    class Meta:
        model = kontakt
        fields = ['Name', 'Email', 'subject', 'message']

class SnusOpret(forms.ModelForm):
    pass

class SnusPost(forms.ModelForm):
    pass