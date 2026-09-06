# Gestión de eventos con Flask y MySQL

Aplicación web formativa para registrar usuarios y administrar eventos mediante una arquitectura organizada en modelos, vistas y controladores.

## Funcionalidades

- registro y validación de usuarios;
- creación, consulta, edición y eliminación de eventos;
- persistencia de datos en MySQL;
- separación de controladores, modelos, plantillas y configuración.

## Tecnologías

- Python
- Flask
- MySQL
- PyMySQL
- HTML / Jinja

## Configuración

Crea las variables de entorno indicadas en `.env.example`. No publiques contraseñas ni claves reales.

Ejemplo en PowerShell:

```powershell
$env:MYSQL_HOST="127.0.0.1"
$env:MYSQL_USER="root"
$env:MYSQL_PASSWORD="tu_contraseña"
$env:MYSQL_DATABASE="esquema_eventos"
$env:FLASK_SECRET_KEY="una_clave_larga_y_aleatoria"
python server.py
```

Antes de iniciar, ejecuta el esquema disponible en `flask_app/db/esquema_eventos.sql`.

## Ejecución local

```bash
python -m venv .venv
pip install flask pymysql
python server.py
```

## Estructura

- `flask_app/controllers/`: rutas y flujo de solicitudes;
- `flask_app/models/`: reglas y consultas de datos;
- `flask_app/templates/`: vistas HTML;
- `flask_app/db/`: esquema de base de datos;
- `server.py`: punto de inicio.

## Estado

Proyecto de aprendizaje. Antes de llevarlo a producción se deben agregar pruebas, manejo centralizado de errores y despliegue seguro.

## Autor

Kenny Bugueño Sotelo  
[LinkedIn](https://www.linkedin.com/in/klbs/) · [GitHub](https://github.com/KennyLincoln)
