from django import forms
from .models import task
from .models import Servicio
from .models import Venta

class taskform(forms.ModelForm):
    class Meta:
        model = task
        fields = ['title','description']
        
        
class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['servicio', 'cliente', 'precio_compra', 'precio_venta', 'fecha_vencimiento', 'observaciones']
        widgets = {
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }
        
        
        