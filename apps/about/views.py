from django.shortcuts import render

# Create your views here.
def about(request):
    context = {"about_page": "active"}
    return render(request, 'about/about.html', context)