from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView as BaseLogoutView, LoginView as BaseLoginView
from .forms import ExtendedUserCreationForm
from .models import House, Apartment, Application
from django.urls import reverse_lazy

# Create your views here.
class StyledLogoutView(BaseLogoutView):
    template_name = 'registration/logout.html'

class CustomLoginView(BaseLoginView):
    success_url = reverse_lazy('profile')

def catalog(request):
    house = House.objects.all()
    return render(request, 'main/catalog.html', {'houses' : house})

@login_required(login_url='/login')
def create(request, apartment_id):
    apartment = get_object_or_404(Apartment, ID=apartment_id)
    user_id = request.user
    application = Application.objects.create(
        UserID = user_id,
        ApartmentID = apartment,
        Status = False
    )
    return render(request, 'main/create.html')

def apartment(request, apartment_id):
    apartment = get_object_or_404(Apartment, ID=apartment_id)
    return render(request, 'main/apartment.html', {'apartment':apartment})

def house(request, house_id):
    house = get_object_or_404(House, ID=house_id)
    apartments = Apartment.objects.filter(HouseID=house)
    return render(request, 'main/house.html', {'house': house, 'apartments': apartments})

def index(request):
    houses = House.objects.all()
    return render(request, 'main/index.html', {'houses' : houses})

def reg(request):
    return render(request, 'main/reg.html')

def kvartira(request):
    kvartiras = Apartment.objects.all()
    return render(request, 'main/kvartiri.html', {'kvartiri' : kvartiras})

def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/profile')
    else:
        form = ExtendedUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def auth(request):
    return render(request, 'main/auth.html')

@login_required(login_url='/login')
def profile(request):
    return render(request, 'registration/profile.html')