from django.contrib import admin
from .models import info
# Register your models here.

class infoadmin(admin.ModelAdmin):
    list_display = ['id','name','city','Comics']

admin.site.register(info,infoadmin)