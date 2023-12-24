from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Quote
# Create your views here.
def quote(request):
    return render(request, 'free_quote/quote.html')



def addQuote(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        services = request.POST['services']
        message = request.POST['message']

        print(name, email, services, message)

        Quote.objects.create(name=name, email=email, services=services, message=message)
        messages.success(request, 'Successfully add The Quote!')
        return redirect('index')

    context = {"quote_page": "active"}
    return render(request, 'contact/contact.html', context)