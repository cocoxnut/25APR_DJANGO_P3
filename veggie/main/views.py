from django.shortcuts import render, redirect
from .models import Product, Contact

def home_page(request):
    context = {
        'product' : Product.objects.all()[:6],
        'starters' : Product.objects.all().filter(category=1),
        'main_dishes': Product.objects.all().filter(category=2),
        'desserts': Product.objects.all().filter(category=3),
        'drinks': Product.objects.all().filter(category=4)
    }
    if request.method == "POST":
        name = request.POST['name']
        email= request.POST['email']
        message = request.POST['message']
        Contact.objects.create(name=name, email=email, message=message)
        return redirect('home')
    return render(request, 'index.html', context)

# Create your views here.
