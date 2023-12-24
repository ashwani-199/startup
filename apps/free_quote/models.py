from django.db import models


SERVICE_CHOICES = ( 
    ("Web Development", "Web Development"), 
    ("Django", "Django"), 
    ("Flask", "Flask"), 
) 
class Quote(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    services = models.CharField(max_length = 20, choices = SERVICE_CHOICES) 
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)