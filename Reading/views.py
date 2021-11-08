from django import forms
from django.shortcuts import render

from Reading.forms import CreateNewReadingBook
from myproject.Reading.models import ReadingBook

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
 #Tạo render cho COURSES
def courses_views(request):
    object_list = ReadingBook.objects.filter()
    
    return render(
        request,
        'courses.html',{
            'object_list':object_list
        }
    )

#Tạo render cho form_LOGIN
def Login(request):
    return render(
        request,
        'login.html',{}
    )