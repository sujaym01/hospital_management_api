from django.contrib import admin
from .models import ContactUs
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'problem']
admin.site.register(ContactUs, ContactAdmin)