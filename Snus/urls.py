from django.urls import path
from . import views

urlpatterns = [
    #path('Kontak/', views.kontakt, name='Site-Kontak'),
    #path('Snus/', views.Snus, name='Site-Snus'),
    path('SnusTest/', views.SnusTest, name='Site-SnusTest'),
]