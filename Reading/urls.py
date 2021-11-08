from django.urls import path

from Reading import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create-newRead/', views.create_news_reading, name='create-news-read'),
    path('courses/', views.courses_views, name='courses-views'),
    path('login/',views.Login, name='login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
