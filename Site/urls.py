from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Site-home'),
    path('test/', views.test, name='Site-test'),
]