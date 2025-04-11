from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import taskform, ServicioForm, VentaForm
from .models import task, Servicio, Venta, Cliente 
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

from django.shortcuts import render
from .models import Venta
from django.db.models import Q

@login_required
def listar_ventas(request):
    ventas = Venta.objects.all()

    # Filtrar por fechas
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    if fecha_inicio:
        ventas = ventas.filter(fecha_venta__gte=fecha_inicio)
    if fecha_fin:
        ventas = ventas.filter(fecha_venta__lte=fecha_fin)

    # Filtrar por cliente
    cliente = request.GET.get('cliente')
    if cliente:
        ventas = ventas.filter(cliente__icontains=cliente)

    # Filtrar por servicio
    servicio = request.GET.get('servicio')
    if servicio:
        ventas = ventas.filter(servicio__nombre__icontains=servicio)

    # Filtrar por usuario
    usuario = request.GET.get('usuario')
    if usuario:
        ventas = ventas.filter(usuario__username__icontains=usuario)

    return render(request, 'crud/lista_ventas.html', {
        'ventas': ventas
    })

from django.db.models import F, Sum


def dashboard_view(request):
    hoy = timezone.now()
    inicio_mes = hoy.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    
    # 1. Cuentas vendidas este mes
    cuentas_vendidas_mes = Venta.objects.filter(
        fecha_venta__gte=inicio_mes
    ).count()
    
    # 2. Ganancias del mes (calcular la diferencia entre precio_venta y precio_compra)
    ganancias_mes = Venta.objects.filter(
        fecha_venta__gte=inicio_mes
    ).aggregate(total=Sum(F('precio_venta') - F('precio_compra')))['total'] or 0
    
    # 3. Cuentas por vencer (próximos 7 días)
    fecha_limite = hoy + timedelta(days=7)
    cuentas_por_vencer = Venta.objects.filter(
        fecha_vencimiento__gte=hoy,
        fecha_vencimiento__lte=fecha_limite
    ).count()
    
    # 4. Total de clientes ÚNICOS (desde el campo cliente de Venta)
    total_clientes = Venta.objects.values('cliente').distinct().count()  # <-- Clave aquí
    
    return render(request, 'dashboard.html', {
        'cuentas_vendidas_mes': cuentas_vendidas_mes,
        'ganancias_mes': ganancias_mes,
        'cuentas_por_vencer': cuentas_por_vencer,
        'total_clientes': total_clientes
    })
