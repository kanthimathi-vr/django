

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm, ContactModelForm

def contact_manual(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save manually if needed
            messages.success(request, "Message sent successfully!")
            return redirect('contact_manual')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()
    return render(request, 'contact_manual.html', {'form': form})


def contact_modelform(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message saved to database!")
            return redirect('contact_modelform')
        else:
            messages.error(request, "Please correct the errors.")
    else:
        form = ContactModelForm()
    return render(request, 'contact_modelform.html', {'form': form})
