from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from crud.views import registrar_venta
from .views import listar_ventas
from .views import dashboard_view
from .views import cuentas_por_vencer
from .views import listar_clientes

app_name = 'crud'

urlpatterns = [
    path('', views.task_list_and_create, name='crud_list'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'), 
    path('servicios/', views.listar_servicios, name='listar_servicios'),
    path('crear-servicio/', views.crear_servicio, name='crear_servicio'),
    path('eliminar-servicio/<int:id>/', views.eliminar_servicio, name='eliminar_servicio'),
    path('registrar-venta/', registrar_venta, name='registrar_venta'),
    path('ventas/', listar_ventas, name='listar_ventas'),
    path('dashboard/', dashboard_view, name='dashboard'),  # Mantén solo esta línea
    path('cuentas_por_vencer/', cuentas_por_vencer, name='cuentas_por_vencer'), 
    path('registrar-cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('listar_clientes/', listar_clientes, name='listar_clientes'),

]
