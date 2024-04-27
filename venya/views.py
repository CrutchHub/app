from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/main.html')

def reg(request):
    return render(request, 'main/register.html')

def order(request):
    return render(request, 'main/order.html')

def catalog(request):
    return render(request, 'main/catalogdiplom.html')

def car(request):
    return render(request, 'main/car.html')

def auth(request):
    return render(request, 'main/auth.html')

def account(request):
    return render(request, 'main/account.html')