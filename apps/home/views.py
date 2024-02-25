from django.shortcuts import render
from apps.blog.models import BlogPost

# Create your views here.
def index(request):
    recent_blog = BlogPost.objects.all().order_by('-id')[:3]
    context = {"home_page": "active", 
               "recent_blog": recent_blog
    }
    return render(request, 'home/index.html', context)