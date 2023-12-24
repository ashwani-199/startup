from django.urls import path
from . import views

urlpatterns = [
    path('', views.quote, name='quotes'), 
    path('add-quote/', views.addQuote, name='add_quote'),
]