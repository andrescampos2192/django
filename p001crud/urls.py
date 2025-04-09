from django.contrib import admin
from django.urls import path, include
from crud.views import register, dashboard  # Asegúrate de que la vista dashboard esté en crud.views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Usamos las vistas de autenticación integradas de Django:
    path('accounts/', include('django.contrib.auth.urls')),
    # Rutas de la app crud (incluye tus rutas personalizadas de registro, login, etc.)
    path('crud/', include('crud.urls', namespace='crud_list')),
    # Ruta para el registro, usando la vista register de la app crud
    path('registration/', register, name='register'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # Eliminamos aquí la inclusión de 'accounts.urls'
    # path('accounts/', include('accounts.urls')),  <-- ¡Elimina esta línea!
    # Ruta para el dashboard (puedes proteger esta vista con @login_required)
    path('dashboard/', dashboard, name='dashboard'),
]
