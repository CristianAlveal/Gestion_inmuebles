from django.contrib import admin
from gestion_inmuebles.models.inmueble import Inmueble
from gestion_inmuebles.models.region import Region
from gestion_inmuebles.models.comuna import Comuna
from gestion_inmuebles.models.usuario import Usuario

@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_inmueble','direccion', 'precio_mensual','comuna')
    search_fields = ('nombre', 'direccion', 'comuna__nombre')
    list_filter = ('tipo_inmueble', 'comuna')
    
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Usuario)