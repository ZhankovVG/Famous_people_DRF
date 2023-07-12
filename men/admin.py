from django.contrib import admin
from .models import *


@admin.register(Men)
class MenAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'time_create', 'time_update', 'is_published')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )