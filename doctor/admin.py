from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.AvailableTime)

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    
admin.site.register(models.Specialization, SpecializationAdmin)
admin.site.register(models.Designation, DesignationAdmin)
admin.site.register(models.Doctor)
admin.site.register(models.Review)




#  w3 schools theke collect kora
# from django.contrib import admin
# from .models import Member

# # Register your models here.

# class MemberAdmin(admin.ModelAdmin):
#   list_display = ("firstname", "lastname", "joined_date",)
#   prepopulated_fields = {"slug": ("firstname", "lastname")}
  
# admin.site.register(Member, MemberAdmin)