from django.contrib import admin
from .models import Address


# Register your models here.

class TestHabitation(admin.ModelAdmin):
    list_display = ('city', 'address', 'country', 'postcode')


admin.site.register(Address, TestHabitation)