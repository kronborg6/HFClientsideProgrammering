from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .forms import CreateUserForm
from Snus.forms import KontaktSender, SnusOpret
from Snus.models import Produt

def home(request):
        if request.method == 'POST':
            if request.POST.get('submit') == 'sign_in':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password=password)
                login(request, user)

                if user is not None:
                    messages.info(request, 'Welcome ' + username)
                    return redirect('Site-Home')

            elif request.POST.get('submit') == 'sign_up':
                aform = CreateUserForm(request.POST)
                if aform.is_valid():
                    aform.save()
                    user = aform.cleaned_data.get('username')
                    messages.success(request, 'Account was created for ' + user)
                    return redirect('Site-Home')

            elif request.POST.get('submit') == 'Produt_create':
                cform = SnusOpret(request.POST)
                if cform.is_valid():
                    cform.save()
                    messages.success(request, 'Produt skal blive godkent af en admin')
                    return redirect('Site-Home')

            elif request.POST.get('submit') == 'kontak_create':
                bform = KontaktSender(request.POST)
                if bform.is_valid():
                    bform.save()
                    messages.success(request, f'Din besked er blevet Modtaget')
                    return redirect('Site-Home')

            else:
                messages.info(request, 'Username OR password is incorrect')
        else:
            aform = CreateUserForm()
            bform = KontaktSender()
            cform = SnusOpret()
            context = {'aform': aform, 'bform': bform, 'cform': cform}
            return render(request, 'Site/Home.html', context)

def test(request):
    return render(request, 'Site/TesTT.html', {'tittle': 'Test'})

def Snus(request):
    context = {
        'posts': Produt.objects.all()
    }
    return render(request, 'Site/SnusList.html', context)
def ProdutSnusTest(request):
    context = {
        'posts': Produt.objects.all()
    }
    return render(request, 'Site/SnusTest.html', context)

@login_required
def logoutUser(request):
    logout(request)
    messages.success(request, 'You have ben Logout! have a nice day')
    return redirect('Site-Home')