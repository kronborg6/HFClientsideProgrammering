from .models import kontakt, Produt
from django.forms import ModelForm
from django import forms

class KontaktSender(forms.ModelForm):
    class Meta:
        model = kontakt
        fields = ['Name', 'Email', 'subject', 'message']

class SnusOpret(forms.ModelForm):
    class Meta:
        model = Produt
        fields = ['Name', 'ProductName', 'NicotineContent', 'Price', 'Description', 'Img']


class SnusPost(forms.ModelForm):
    pass