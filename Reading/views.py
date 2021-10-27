from django import forms
from django.shortcuts import render

from myproject.Reading.forms import CreateNewReadingBook

#Tạo render cho HOME
def home_view(request):
    return render(
        request,
        'home.html',{}
    )

#Tạo render cho CREATE_READ_NEWS

def create_news_reading(request):
    if request.method == 'POST':
        pass
    else:
        form = CreateNewReadingBook()
        
    return render(
        request,
        'New_Read.html',
        {
            'form' : form
        }
    )

