from django.shortcuts import render, redirect
from django.contrib import messages
from .models import kontakt
from .forms import KontaktSender
from django.contrib.auth.decorators import login_required

def kontakt(request):
    if request.method == 'GET':
        form = KontaktSender()
    else:
        form = KontaktSender(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Din besked er blevet Modtaget')
            return redirect('Site-Home')

    return render(request, "Snus/Kontakt.html", {'form': form})

@login_required
def AddProdut(request):
    pass
