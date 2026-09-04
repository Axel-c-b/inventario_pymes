"""
Configuración de URLs del proyecto core.

El proyecto delega todas las rutas de la aplicación al archivo
inventario/urls.py mediante include(), manteniendo separadas las rutas
propias del núcleo (por ejemplo /admin/) de las rutas de la aplicación.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventario.urls')),
]

# Vista personalizada para el error 404, controlada por la aplicación.
# Solo se muestra cuando DEBUG = False (ver README.md).
handler404 = 'inventario.views.pagina_no_encontrada'
