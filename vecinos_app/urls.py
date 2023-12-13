from django.urls import path
from .views import index, info_socios, buscar_socio
from vecinos_app.views import index  # Asegúrate de que la ruta sea correcta según la ubicación de tu views.py


urlpatterns =[
    #path('',homeView, name='home'),
    #path('perfil/', views.perfil),
    path('index/', index, name='index'),
    path('inicio/', info_socios, name='inicio'),
    path('buscar_socio/',buscar_socio, name='buscar_socio'),
    
]




