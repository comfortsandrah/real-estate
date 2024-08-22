from django.shortcuts import render
from . import forms


# Create your views here.
def home(request):
    return render(request, "index.html")


def contact(request):
    context = {"title": "Contact Us", "form": forms.ContactForm()}
    return render(request, "contact.html", context=context)

def about(request):
    return render(request, "about.html")