from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'Site/Home.html', {'title': 'Home'})

def test(request):
    return render(request, 'Site/Test.html', {'tittle': 'Test'})