from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    search_fields = ["name", "email"]
    list_filter = ["name", "email"]


@admin.register(models.Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ["name", "pricing", "created_at", "updated_at"]
    search_fields = ["name", "pricing"]
    list_filter = ["name", "pricing", "created_at", "updated_at"]
    date_hierarchy = "created_at"
    ordering = ["-created_at", "-updated_at"]
