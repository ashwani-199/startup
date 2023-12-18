from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'), 
    path('blogDetail/', views.blogDetail, name='blogDetail'),
]