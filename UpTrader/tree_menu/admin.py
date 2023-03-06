from django.contrib import admin
from .models import CategoryModel


@admin.register(CategoryModel)
class AdminCategory(admin.ModelAdmin):
    list_display = ['title', 'parent']


