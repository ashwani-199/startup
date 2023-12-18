from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'blog/blog.html')

def blogDetail(request):
    return render(request, 'blog/detail.html')