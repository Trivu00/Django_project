from django import forms
from django.db import models
from django.forms import fields
from Reading.models import ReadingBook

class CreateNewReadingBook(forms.ModelForm):
    class Meta : 
        model = ReadingBook
        fields = (
            'name',
            'read_write',
            'name_id',
            'author',
        )