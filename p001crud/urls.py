from django.contrib import admin
from django.urls import path, include
from crud.views import register



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Agregado para las vistas de login, logout, etc.
    path('crud/', include('crud.urls', namespace='crud_list')),
    path('registration/', register, name='register'),
]
