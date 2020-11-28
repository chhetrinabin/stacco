
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm


def contact(request):
   
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Message sent successfully!')
            return redirect('home')
    form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})