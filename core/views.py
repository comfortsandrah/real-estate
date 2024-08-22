from django.shortcuts import get_object_or_404, render
from . import forms
from django.contrib import messages
from . import models


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


def property_listing(request):
    properties = models.Property.objects.all()

    category = request.GET.get("category")
    location = request.GET.get("location")
    max_price = request.GET.get("max-price")

    # Perform your filtering logic based on the parameters
    if category:
        properties = properties.filter(category=category)

    if location:
        properties = properties.filter(
            location__icontains=location, name__icontains=location
        )

    if max_price:
        properties = properties.filter(pricing__lte=max_price)

    context = {
        "properties": properties,
    }
    return render(request, "properties.html", context=context)


def property_detail(request, id):
    property = get_object_or_404(models.Property, id=id)
    context = {
        "property": property,
    }
    return render(request, "tour.html", context=context)


def book_virtual_tour(request):
    context = {}
    return render(request, "book_virtual_tour.html", context=context)


def about(request):
    context = {}
    return render(request, "about.html", context=context)
