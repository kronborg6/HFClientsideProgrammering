from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Produt
from .forms import KontaktSender, SnusOpret
from django.contrib.auth.decorators import login_required
from Site.forms import CreateUserForm
from django.shortcuts import render, redirect

"""
def kontakt(request):
    if request.method == 'GET':
        form = KontaktSender()
    else:
        bform = KontaktSender(request.POST)
        if bform.is_valid():
            bform.save()
            messages.success(request, f'Din besked er blevet Modtaget')
            return redirect('Site-Home')

    return render(request, "Snus/Kontakt.html", {'form': form})


def Snus(request):
    context = {
        'posts': Produt.objects.all()
    }
    return render(request, 'Snus/ProdutTest2.html', context)
    """

#@login_required
def SnusTest(request):
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
            if request.user.is_authenticated:
                cform = SnusOpret(request.POST)
                if cform.is_valid():
                    cform.save()
                    messages.success(request, 'Produt skal blive godkent af en admin')
                    return redirect('Site-Home')
            else:
                messages.error(request, 'Du er ikke logget in')
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
        context = {'aform': aform, 'bform': bform, 'cform': cform, 'posts': Produt.objects.all()}
        return render(request, 'Snus/ProdutTest2.html', context)


@login_required
def AddProdut(request):
    pass
