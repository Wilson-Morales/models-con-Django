from django.db import models

# Create your models here.


class Clinica (models.Model):
    nombre = models.CharField(max_length=30)
    tipo =   models.CharField(max_length=20)
    direccion = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=30)
       
    def __str__(self):
        return "%s %s %s %s" % (self.nombre, self.tipo, self.direccion, self.ciudad)
    



class Consultorio (models.Model):
    nombre_doctor = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30)
    valor_consulta = models.IntegerField()
    clinica = models.ForeignKey(Clinica, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s %s %s %s" % (self.nombre_doctor, self.especialidad, self.valor_consulta, self.clinica)
