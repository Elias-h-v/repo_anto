# Paso:1 Redirigete a la carpeta del proyecto con CD, si está en MacOS debe usar "/"
 
# Paso 2: Cree el ambiente virtual
python -m venv envsia

# Paso 3: Activar el entorno virtual
envsia\Scripts\activate

# Paso 4: Instalar las librerias del archivo requirements.txt
pip install -r requirements.txt

# Paso 5: Crear nuevo proyecto
django-admin startproject project_vecinos .
django-admin startapp vecinos_app  
# Paso 6: abrir el proyecto
cd myproject
# crear superususario
python manage.py createsuperuser

# Paso 7: Hacer migraciones
python manage.py makemigrations
# Paso 8: Iniciar las migraciones
python manage.py migrate

# Paso 9: Ejecutar la aplicación manage.py
python manage.py runserver

# Pas 10: crear las class de tu base de datos
python manage.py inspectdb > models.py