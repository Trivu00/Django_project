from django.contrib import admin
from django.contrib.admin.filters import ListFilter

from Reading.models import ReadingBook, Category

@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ReadingBook)
class ReadBookAdmin(admin.ModelAdmin):
    list_display = ('name','name_id','read_write','author',)
    Search = ('name','author',)
    ListFilter = ('name-id',)
    
