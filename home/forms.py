from django import forms

class CreacionProfesional(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    anos_experiencia = forms.IntegerField(required=True)

class CreacionCortePelo(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    precio = forms.DecimalField(required=True)
    tiempo = forms.IntegerField(required=True)
    
class CreacionCliente(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)