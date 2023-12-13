from django.shortcuts import render
from .models import Socios
from django.http import HttpResponse


def index(request):
    return render(request, 'vecinos_app/index.html')

def info_socios(request):
    socios_lista = Socios.objects.all().order_by('rut')
    return render(request, "info_socio.html", {"Socios": socios_lista})

def buscar_socio(request):
    certificado_data = {}
    mensaje_error = ""

    if request.method == 'POST':
        rut_busqueda = request.POST.get('rut_busqueda')

        try:
            socio = Socios.objects.get(rut=rut_busqueda)

            # Devolver solo los datos necesarios
            certificado_data = {
                "rut": socio.rut,
                "nombre": socio.nombre,
                "apellido": socio.apellido,
                "direccion": socio.direccion,
                "fecha": socio.fecha_nacimiento,
            }

        except Socios.DoesNotExist:
            mensaje_error = "No se encontró al socio con el rut proporcionado."

    return render(request, "buscar_socio.html", {"certificado_data": certificado_data, "mensaje_error": mensaje_error})