from django import forms
from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control"}),
        }
