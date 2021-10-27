from django.urls import path

from Reading import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create-newRead/', views.create_news_reading, name='create-news-read'),
    
]