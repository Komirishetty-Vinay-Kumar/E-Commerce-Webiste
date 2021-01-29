from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Registration,Product,Contact
from .forms import LoginForm
from .forms import RegistrationForm
from math import ceil

def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("valid Details")
            return redirect('login')
    else:
        form = RegistrationForm()
        print("Invalid Details")
    return render(request, 'registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            un = request.POST.get('username')
            pwd = request.POST.get('password')
            dbuser = Registration.objects.filter(username=un, password=pwd)
            if not dbuser:
                return HttpResponse("Login Failed")
            else:
                return render(request,"about.html")
        else:
            form = LoginForm(request.POST)
            return render(request, 'personal_details', {'form': form})
    else:
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, 'home.html')







def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    #return render(request, 'index.html', params)

    return render(request, 'welcome.html', params)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        c = Contact(name=name, email=email, phone=phone, desc=desc)
        c.save()
    return render(request, 'contact.html')

def tracker(request):
    return render(request, 'search.html')

def search(request):
    return render(request, 'search.html')

def productView(request,myid):
    product = Product.objects.filter(id=myid)

    return render(request, 'prodView.html',{'product':product[0]})

def checkout(request):
    return render(request, 'checkout.html')



