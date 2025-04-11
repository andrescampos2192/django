from django.contrib import admin
from django.urls import path, include
from crud.views import register, dashboard  # Asegúrate de que la vista dashboard esté en crud.views
from django.views.generic import TemplateView
from crud.views import crear_servicio
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from crud.views import crear_servicio
from crud.views import registrar_venta
from crud.views import dashboard_view
from crud.views import cuentas_por_vencer
from crud.views import listar_clientes

urlpatterns = [
    path('admin/', admin.site.urls),
    # Usamos las vistas de autenticación integradas de Django:
    # Rutas de la app crud (incluye tus rutas personalizadas de registro, login, etc.)
    path('crud/', include('crud.urls', namespace='crud_list')),
    path('registration/', register, name='register'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('dashboard/', dashboard_view, name='dashboard'),  # Mantén esta línea
    path('crear-servicio/', crear_servicio, name='crear_servicio'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('registrar-venta/', registrar_venta, name='registrar_venta'),
    path('cuentas_por_vencer/', cuentas_por_vencer, name='cuentas_por_vencer'), 
    path('listar_clientes/', listar_clientes, name='listar_clientes'),
]
