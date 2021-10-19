from django.forms import ModelForm
from .models import*
from .models import Producto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'email', 'password1','password2']


class Producto_Form(ModelForm):
    class Meta:
        model =   Producto
        fields =  ['codigo', 'nombre', 'precio', 'fecha_vencimiento' ,'especificaciones', 'peso', 'foto', 'categoria']       