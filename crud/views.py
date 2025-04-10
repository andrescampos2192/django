from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import taskform, ServicioForm, VentaForm
from .models import task, Servicio, Venta
from django.db.models import Sum
from django.utils.timezone import now
from datetime import timedelta
from django.utils import timezone




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

def eliminar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    servicio.delete()
    return redirect('listar_servicios')


from django.contrib import messages  # Asegúrate de importar esto

@login_required
def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.fecha_compra = timezone.now()
            venta.fecha_venta = timezone.now()
            venta.usuario = request.user
            venta.save()
            messages.success(request, '¡Venta registrada exitosamente!')
            return redirect('crud:registrar_venta')  # Te mantiene en la misma página
    else:
        form = VentaForm()

    return render(request, 'crud/registrar_venta.html', {'form': form})

def listar_ventas(request):
    ventas = Venta.objects.all().order_by('-fecha_venta')  # Ordena de más reciente a más antigua
    return render(request, 'crud/lista_ventas.html', {'ventas': ventas})


def dashboard_view(request):
    hoy = timezone.now().date()  # Define la variable hoy
    inicio_mes = hoy.replace(day=1)  # Calcula el primer día del mes

    cuentas_vendidas_mes = Venta.objects.filter(fecha_venta__gte=inicio_mes).count()
    ganancias_mes = Venta.objects.filter(fecha_venta__gte=inicio_mes).aggregate(Sum('precio_venta'))['precio_venta__sum'] or 0
    cuentas_por_vencer = Venta.objects.filter(fecha_vencimiento__range=[hoy, hoy + timedelta(days=7)]).count()
    total_clientes = Venta.objects.values('cliente').distinct().count()

    print("Hoy:", hoy)
    print("Inicio del mes:", inicio_mes)
    print("Cuentas vendidas este mes:", cuentas_vendidas_mes)
    print("Ganancias este mes:", ganancias_mes)
    print("Cuentas por vencer:", cuentas_por_vencer)
    print("Total de clientes:", total_clientes)

    return render(request, 'dashboard.html', {
        'cuentas_vendidas_mes': cuentas_vendidas_mes,
        'ganancias_mes': ganancias_mes,
        'cuentas_por_vencer': cuentas_por_vencer,
        'total_clientes': total_clientes
    })

