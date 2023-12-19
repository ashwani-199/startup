from django.shortcuts import render

# Create your views here.
def services(request):
    context = {"services_page": "active"}
    return render(request, 'services/service.html', context)