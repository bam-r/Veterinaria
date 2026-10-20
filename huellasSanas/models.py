from django.db import models

class Mascota(models.Model):
    nombre=models.CharField(max_length=50)
    especie=models.CharField(max_length=30)
    raza=models.CharField(max_length=30)
    dueño=models.CharField(max_length=50)
    
class Cita(models.Model):
    mascota= models.ForeignKey(Mascota, on_delete=models.CASCADE,)
    fecha=models.DateField()
    hora=models.DateTimeField()
    motivo=models.TextField()
    estado= [
        "pendiente",
        "atendida",
        "cancelada",
    ]
    
    