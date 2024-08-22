from django.db import models
from django.urls import reverse


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name + " - " + self.email


class Property(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    pricing = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(
        upload_to="properties/", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("core:property-detail", kwargs={"id": self.pk})
    