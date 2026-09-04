from django.shortcuts import render


def bienvenida(request):
    """
    Vista principal del proyecto.

    Reemplaza la página de bienvenida por defecto de Django y presenta
    el propósito del Sistema de Inventario para PYMEs.
    """
    contexto = {
        'nombre_proyecto': 'Sistema de Inventario para PYMEs',
        'descripcion': (
            'Plataforma para centralizar la gestión de inventario de una '
            'empresa comercial: productos, stock, movimientos y proveedores, '
            'con historial de operaciones y control de reglas de negocio.'
        ),
        'actores': ['Administrador', 'Proveedor'],
    }
    return render(request, 'inventario/bienvenida.html', contexto)


def pagina_no_encontrada(request, exception=None):
    """
    Vista personalizada para el error 404.

    Se registra como handler404 en core/urls.py y se muestra cuando
    DEBUG = False y la ruta solicitada no coincide con ninguna URL
    registrada en el proyecto.
    """
    return render(request, '404.html', status=404)
