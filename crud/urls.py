from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'crud'  # Namespace para las URLs de crud

urlpatterns = [
    # Rutas de la funcionalidad CRUD existente
    path('', views.task_list_and_create, name='crud_list'),
    
    # Rutas de autenticación
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='crud/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
