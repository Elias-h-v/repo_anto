from django.contrib import admin
from django.urls import path, include
from vecinos_app.views import index  # Importa la vista 'index' desde tu aplicación

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vecinos_app/', include('vecinos_app.urls')),
    path('', index, name='index'),  # Usa la vista importada aquí
]
