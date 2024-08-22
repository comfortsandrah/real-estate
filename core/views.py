from django.shortcuts import render
from . import forms
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, "index.html")


def contact(request):
    context = {"title": "Contact Us", "form": forms.ContactForm()}
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Your message has been sent successfully!")
    return render(request, "contact.html", context=context)


def about(request):
    return render(request, "about.html")
