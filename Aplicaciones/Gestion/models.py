from django.db import models

# Create your models here.
class Negocio(models.Model):
    id_negocio = models.PositiveSmallIntegerField(primary_key=True)
    nombre_neg = models.CharField(max_length=80)

    def __str__(self):
        return "{0}".format(self.nombre_neg)



class Departamento(models.Model):
    id_departamento = models.PositiveSmallIntegerField(primary_key=True)
    nombre_dep = models.CharField(max_length=80)
    regiones = [
        ('NT', 'NORTE'),
        ('CT', 'CENTRO'),
        ('SR', 'SUR'),
        ('OR', 'ORIENTE'),
        ('OC', 'OCCIDENTE')
    ]
    region = models.CharField(max_length=2, choices=regiones, default='NT')

    def __str__(self):
        return "{0}".format(self.nombre_dep)

class Municipio(models.Model):
    id_municipio = models.PositiveSmallIntegerField(primary_key=True)
    nombre_mun = models.CharField(max_length=100)

    def __str__(self):
        return "{0}".format(self.nombre_mun)

class Departamento_municipio(models.Model):
    id_departamento_municipio = models.PositiveSmallIntegerField(primary_key=True)
    id_departamento = models.ForeignKey(Departamento, null=False, blank=False, on_delete=models.CASCADE)
    id_municipio = models.ForeignKey(Municipio, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} ({1})".format(self.id_departamento, self.id_municipio)

class Sucursal(models.Model):
    id_sucursal = models.PositiveSmallIntegerField(primary_key=True)
    id_negocio = models.ForeignKey(Negocio, null=False, blank=False, on_delete=models.CASCADE)
    id_departamento_municipio = models.ForeignKey(Departamento_municipio, null=False, blank=False, on_delete=models.CASCADE)
    nombre_suc = models.CharField(max_length=80)
    telefono = models.CharField(max_length=8)

    def __str__(self):
        return "({0}) {1}".format(self.id_negocio, self.nombre_suc)

class Queja(models.Model):
    id_queja = models.AutoField(primary_key=True)
    id_departamento_municipio = models.ForeignKey(Departamento_municipio, null=False, blank=False, on_delete=models.CASCADE)
    id_sucursal = models.ForeignKey(Sucursal, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateField()
    queja = models.CharField(max_length=256)

    def __str__(self):
        return "{0}".format(self.id_sucursal)