from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'), 
    path('blogDetail/<int:id>/', views.blogDetail, name='blogDetail'),
    path('comments/<int:id>/', views.commentsPost, name='comments'), 
]