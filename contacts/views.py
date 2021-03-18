from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

# Create your views here.
def enquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        message = request.POST['message']
        email = request.POST['email']

        contact = Contact(
            car_id = car_id,
            car_title = car_title,
            user_id = user_id,
            first_name = first_name,
            last_name = last_name,
            customer_need = customer_need,
            city = city,
            state = state,
            email = email,
            phone = phone,
            message = message,
        )

        contact.save()
        messages.success(request, "Your request has been submitted !! we will get back to you shortly")
        return redirect('/cars/'+car_id)