from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import crear_servicio
from django.contrib.auth.views import LogoutView
from .views import listar_servicios, eliminar_servicio




app_name = 'crud'

urlpatterns = [
    path('', views.task_list_and_create, name='crud_list'),
    path('register/', views.register, name='register'),
    # otras rutas...
     path('login/', auth_views.LoginView.as_view(), name='login'),
     path('logout/', views.custom_logout, name='logout'),
     path('servicios/', views.lista_servicios, name='lista_servicios'),
    path('servicios/nuevo/', views.crear_servicio, name='crear_servicio'),
    path('crear-servicio/', crear_servicio, name='crear_servicio'),
path('eliminar-servicio/<int:servicio_id>/', eliminar_servicio, name='eliminar_servicio'),
path('servicios/', views.lista_servicios, name='listar_servicios'),




    

]
