from django.shortcuts import render, redirect  # No olvides importar redirect
from .models import task
from .forms import taskform
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ServicioForm
from .models import Servicio
from django.shortcuts import render, redirect, get_object_or_404


def task_list_and_create(request):
    if request.method == 'POST':
        form = taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:crud_list')
    else:
        form = taskform()
    
    tasks = task.objects.all()

    return render(request, 'task_list.html', {
        'form': form,
        'tasks': tasks
    })
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # o al nombre correcto de tu vista de login
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('home')  # O donde tú prefieras redirigir

@login_required
def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_servicios')
    else:
        form = ServicioForm()
    return render(request, 'crud/crear_servicio.html', {'form': form})

@login_required
def lista_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'crud/lista_servicios.html', {'servicios': servicios})


@login_required
def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirige al dashboard o donde tú quieras
    else:
        form = ServicioForm()
    
    return render(request, 'crud/crear_servicio.html', {'form': form})


@login_required
def listar_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'crud/lista_servicios.html', {'servicios': servicios})

@login_required
def eliminar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)
    servicio.delete()
    return redirect('listar_servicios')
