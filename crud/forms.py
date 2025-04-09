from django import forms
from .models import task
from .models import Servicio

class taskform(forms.ModelForm):
    class Meta:
        model = task
        fields = ['title','description']
        
        
class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion']
