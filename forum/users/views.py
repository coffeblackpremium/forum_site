from django.shortcuts import render
from .forms import UsuarioForm

# Create your views here.

def user_register(request):
    form = UsuarioForm
    return render(request, 'register.html', {'form': form})