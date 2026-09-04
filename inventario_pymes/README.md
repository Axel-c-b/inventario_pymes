# Sistema de Inventario para PYMEs

Aplicación web construida con **Python + Django** para centralizar la gestión
de inventario de una empresa comercial: productos, stock, movimientos y
proveedores, manteniendo historial de operaciones, control de reglas de
negocio y trazabilidad para auditoría.

Esta primera entrega corresponde a la **Evaluación 1 (Backend con Python y
Django)**: repositorio, ambiente virtual, núcleo Django y aplicación inicial
funcional. El modelo de datos, migraciones y CRUD se incorporarán en la
siguiente evaluación.

## Actores principales

- **Administrador**: gestiona productos, stock y reglas del sistema.
- **Proveedor**: interactúa con el sistema registrando y consultando
  información asociada a sus productos.

## Estructura del proyecto

```
inventario_pymes/
├── core/                   # Núcleo del proyecto Django (settings, urls)
├── inventario/              # Aplicación principal
│   ├── templates/inventario/bienvenida.html
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── admin.py
├── templates/404.html       # Página de error 404 personalizada
├── manage.py
├── requirements.txt
└── .gitignore
```

## Requisitos previos

- Python 3.11 o superior instalado.
- Git instalado.

## Instalación y ejecución local

1. **Clonar el repositorio**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd inventario_pymes
   ```

2. **Crear el ambiente virtual**
   ```bash
   python -m venv .venv
   ```

3. **Activar el ambiente virtual**

   En Windows (PowerShell):
   ```powershell
   .venv\Scripts\Activate
   ```

   En macOS / Linux:
   ```bash
   source .venv/bin/activate
   ```

   > Si el terminal no permite ejecutar el script de activación en Windows,
   > ejecuta primero: `Set-ExecutionPolicy Bypass -Scope CurrentUser`

4. **Instalar las dependencias**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. **Ejecutar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

6. **Abrir la aplicación**

   Visita [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en tu navegador.
   Debe aparecer la página de bienvenida del Sistema de Inventario para PYMEs
   (no la página por defecto de Django).

## Cómo probar la página 404 personalizada

Django solo muestra la plantilla `404.html` personalizada cuando
`DEBUG = False`. Para probarla en local:

1. En `core/settings.py`, cambia temporalmente `DEBUG = True` por
   `DEBUG = False`.
2. Verifica que `ALLOWED_HOSTS` incluya `'localhost'` y `'127.0.0.1'`
   (ya viene configurado así).
3. Ejecuta nuevamente `python manage.py runserver` y visita una ruta que no
   exista, por ejemplo [http://127.0.0.1:8000/ruta-inexistente/](http://127.0.0.1:8000/ruta-inexistente/).
4. Deberías ver la página 404 personalizada en lugar del error de depuración
   de Django.
5. Vuelve a dejar `DEBUG = True` para continuar desarrollando.

## Dependencias

Ver [`requirements.txt`](requirements.txt).

## Próximos pasos (siguiente evaluación)

- Diseño del modelo de datos (productos, categorías, proveedores,
  movimientos de stock).
- Migraciones y persistencia.
- CRUD y validación de reglas de negocio.
- Registro histórico de cambios de estado para auditoría.
- Consultas con distintos criterios de búsqueda e indicadores de gestión.
