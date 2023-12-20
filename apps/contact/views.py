from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact



def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        messages.success(request, 'Successfully Sent The Message!')
        return redirect('index')

    context = {"contact_page": "active"}
    return render(request, 'contact/contact.html', context)