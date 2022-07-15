from django.contrib import admin

# Register your models here.

from aplicacion.models import Clinica, Consultorio

class ClinicaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'direccion', 'ciudad')
    
    search_fields = ('nombre','ciudad')
    
admin.site.register(Clinica,ClinicaAdmin)



class ConsultorioAdmin(admin.ModelAdmin):
    
    list_display = ('nombre_doctor', 'especialidad', 'valor_consulta', 'get_clinica')
    
    raw_id_fields = ('clinica',)
    
    def get_clinica(self, obj):
        """" """
        return obj.clinica.ciudad
    
admin.site.register(Consultorio,ConsultorioAdmin)