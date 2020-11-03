from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Site-Home'),
    path('logout/', views.logoutUser, name='logout'),
    path('Produt/', views.Snus, name='Site-Produt'),
    path('SnusTest/', views.ProdutSnusTest, name='Site-SnusTest'),
]