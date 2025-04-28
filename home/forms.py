from django import forms
from home.models import Profesional

class CreacionProfesional(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    anos_experiencia = forms.IntegerField(required=True)
    avatar = forms.ImageField(required=False)
    fecha_ingreso = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    
class FormularioModificarProfesional(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = ["nombre", "apellido", "anos_experiencia", "avatar", "fecha_ingreso"]
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
        }

class CreacionCortePelo(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    precio = forms.DecimalField(required=True)
    tiempo = forms.IntegerField(required=True)
    
class CreacionCliente(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)