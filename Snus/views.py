from django.shortcuts import render, redirect
from django.contrib import messages
from .models import kontakt

def kontakt(request):
    if request.method == 'GET':
        form = kontakt()
    else:
        form = MailSender(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Din besked er blevet Modtaget')
            return redirect('web-home')

    return render(request, "Snus/Kontakt.html", {'form': form})
