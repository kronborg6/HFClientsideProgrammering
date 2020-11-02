from django.urls import path
from . import views

urlpatterns = [
    path('Kontak/', views.kontakt, name='Site-Kontak'),
    path('Produt/', views.Produt, name='Site-Produt'),
]