from django import forms
# se invoca a la funcion de django para creacion de formularios para registro
from django.contrib.auth.forms import UserCreationForm
# se importa el modelo por defeco de django
from django.contrib.auth.models import User

# se agrega una clase para agregar un nuevo campo email al formulario
class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']