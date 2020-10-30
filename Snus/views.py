from django.shortcuts import render, redirect
from django.contrib import messages
from .models import kontakt
from .forms import KontaktSender
from django.contrib.auth.decorators import login_required
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
"""
@login_required
def AddProdut(request):
    pass
