from django.db import models

class Profesional(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    anos_experiencia = models.IntegerField()
    avatar = models.ImageField(upload_to="profesionales", null=True, blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)
    
    def __str__(self):
        unidad = "Año" if self.anos_experiencia == 1 else "Años"
        return f'{self.nombre} {self.apellido} - Experiencia: {self.anos_experiencia} {unidad}'
    
class CortePelo(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo = models.IntegerField()
    
    def __str__(self):
        return f'${self.precio} - Corte: {self.nombre} - Tiempo estimado: {self.tiempo} minutos'
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - Contacto: {self.email}'