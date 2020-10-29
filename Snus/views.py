from django.shortcuts import render, redirect
from django.contrib import messages
from .models import kontakt
from .forms import KontaktSender

def kontakt(request):
    if request.method == 'GET':
        form = KontaktSender()
    else:
        form = KontaktSender(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Din besked er blevet Modtaget')
            return redirect('web-home')

    return render(request, "Snus/Kontakt.html", {'form': form})
