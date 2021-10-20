from django.shortcuts import render
from .forms import UsuarioForm

# Create your views here.

def usuario_registro(request):
    form = UsuarioForm
    return render(request, 'register.html', {'form': form})

def usuario_login(parameter_list):
    pass

def dashboard(parameter_list):
    pass
