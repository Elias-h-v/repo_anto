from django.contrib import admin

# Register your models here.
from .models import (
    Certificados,
    Comisiones,
    GruposFamiliares,
    Parentescos,
    Perfiles,
    Socios,
    TipoCertificados,
    TipoComisiones
)
class SociosAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido')
    ordering = ('rut',)
    search_fields =('rut',)
    list_display_links = ('rut',)
    list_filter = ('id_perfil',)
    list_per_page = 15

admin.site.register(Certificados)
admin.site.register(Comisiones)
admin.site.register(GruposFamiliares)
admin.site.register(Parentescos)
admin.site.register(Perfiles)
admin.site.register(TipoCertificados)
admin.site.register(TipoComisiones)
admin.site.register(Socios, SociosAdmin)