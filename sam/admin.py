from django.contrib import admin

from sam.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id","username","first_name","last_name","email")

