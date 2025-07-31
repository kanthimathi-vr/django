

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterForm, NewsletterModelForm
from .models import Subscriber

def newsletter_manual(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            Subscriber.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email']
            )
            messages.success(request, "You have subscribed successfully!")
            return redirect('newsletter_manual')
        else:
            messages.error(request, "Please fix the errors.")
    else:
        form = NewsletterForm()
    return render(request, 'newsletter_manual.html', {'form': form})

def newsletter_model(request):
    if request.method == 'POST':
        form = NewsletterModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have subscribed successfully!")
            return redirect('newsletter_model')
        else:
            messages.error(request, "Please fix the errors.")
    else:
        form = NewsletterModelForm()
    return render(request, 'newsletter_model.html', {'form': form})
