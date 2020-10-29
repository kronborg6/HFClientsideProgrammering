from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib import messages

def home(request):
    return render(request, 'Site/Home.html', {'title': 'Home'})

def test(request):
    return render(request, 'Site/Test.html', {'tittle': 'Test'})

@login_required
def logoutUser(request):
    logout(request)
    messages.success(request, 'You have ben Logout! have a nice day')
    return redirect('Site-Home')