from django.contrib import admin

from .models import Task, User

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "complete", "created_on")
    list_display_links = ("title",)
    
