from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("properties/", views.property_listing, name="property-listing"),
    path("properties/<int:id>", views.property_detail, name="property-detail"),
]
