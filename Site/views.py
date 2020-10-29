from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

def home(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, 'Welcome ' + username)
                return redirect('Site-Home')

            else:
                messages.info(request, 'Username OR password is incorrect')
        return render(request, 'Site/Home.html', {'title': 'Home'})

def test(request):
    return render(request, 'Site/Test.html', {'tittle': 'Test'})

@login_required
def logoutUser(request):
    logout(request)
    messages.success(request, 'You have ben Logout! have a nice day')
    return redirect('Site-Home')