from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Site-Home'),
    path('test/', views.test, name='Site-test'),
]