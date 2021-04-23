from django.contrib import admin
from Gestion.models import Negocio, Departamento, Municipio, Departamento_municipio, Sucursal, Queja
# Register your models here.

admin.site.register(Negocio)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Departamento_municipio)
admin.site.register(Sucursal)
admin.site.register(Queja)