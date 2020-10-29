from .models import kontakt
from django.forms import ModelForm
from django import forms

class KontaktSender(forms.ModelForm):
    class Meta:
        model = kontakt
        fields = ['FullName', 'Email', 'subject', 'message']