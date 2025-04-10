from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from crud.views import registrar_venta, dashboard_view
from .views import listar_ventas

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
    path('dashboard/', views.dashboard_view, name='dashboard'),

]
