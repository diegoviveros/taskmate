from django.shortcuts import render, redirect
# se invoca a la funcion de django para creacion de formularios para registro
#from django.contrib.auth.forms import UserCreationForm

# importar mensajero de django
from django.contrib import messages
from .forms import CustomRegisterForm

# Create your views here.
def register(request):
    if request.method=="POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New user Account Created, Login to get started!"))
            return redirect('register')
    else:     
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})