from django.contrib import admin
from .models import task

@admin.register(task)
class taskAdmin(admin.ModelAdmin):
    list_display =['title','created']
