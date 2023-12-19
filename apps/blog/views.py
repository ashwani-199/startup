from django.shortcuts import render

# Create your views here.
def blog(request):
    context = {"blog_page": "active"}
    return render(request, 'blog/blog.html', context)

def blogDetail(request):
    context = {"detail_page": "active"}
    return render(request, 'blog/detail.html', context)