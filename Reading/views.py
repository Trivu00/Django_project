
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from Reading.forms import CreateNewReadingBook, RegistrationForm
from Reading.models import ReadingBook





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
    object_list = ReadingBook.objects.all()
    
    return render(
        request,
        'courses.html',{
            'object_list':object_list,
        }
    )

#Tạo render cho form_LOGIN
def Login(request):
    return render(
        request,
        'login.html',{}
    )

#Tạo render cho form Profile
@login_required
def Profile(request):
    return render(
        request,
        'profile.html',{}
    )

#Tạo render cho REGISTER


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'register.html', {'form': form})
