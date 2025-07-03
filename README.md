# 📋 CRUD Django - Sistema de Gestión de Tareas

Un sistema completo de gestión de tareas desarrollado con Django que permite a los usuarios crear, gestionar y organizar sus tareas personales. Este proyecto demuestra la implementación de operaciones CRUD (Create, Read, Update, Delete) con autenticación de usuarios.

## ✨ Características

- 🔐 **Sistema de Autenticación**: Registro, login y logout de usuarios
- 📝 **Gestión de Tareas**: Crear, editar, eliminar y marcar como completadas
- ⭐ **Tareas Importantes**: Marcar tareas como prioritarias
- 👤 **Usuarios Individuales**: Cada usuario ve solo sus propias tareas
- 📅 **Fechas Automáticas**: Registro de creación y completado de tareas
- 🎨 **Interfaz Moderna**: Diseño responsivo con Tailwind CSS
- 🔒 **Seguridad**: Autenticación requerida para todas las operaciones

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 5.2
- **Base de Datos**: SQLite
- **Frontend**: HTML, CSS (Tailwind CSS)
- **Autenticación**: Django Auth System
- **Formularios**: Django Forms

## 📋 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/CRUD-DJANGO-TAREAS.git
   cd CRUD-DJANGO-TAREAS
   ```

2. **Crea un entorno virtual**
   ```bash
   python -m venv venv
   ```

3. **Activa el entorno virtual**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Instala las dependencias**
   ```bash
   pip install django
   ```

5. **Ejecuta las migraciones**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crea un superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Inicia el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

8. **Abre tu navegador y ve a**
   ```
   http://127.0.0.1:8000/
   ```

## 📖 Uso

### Registro y Autenticación
1. Ve a `/registro/` para crear una nueva cuenta
2. Completa el formulario con tu nombre de usuario, email y contraseña
3. Inicia sesión en `/login/` con tus credenciales

### Gestión de Tareas
- **Crear Tarea**: Ve a `/tasks/create/` y completa el formulario
- **Ver Tareas**: Accede a `/tasks/` para ver todas tus tareas pendientes
- **Editar Tarea**: Haz clic en una tarea para editarla
- **Completar Tarea**: Marca una tarea como completada
- **Eliminar Tarea**: Elimina tareas que ya no necesites

## 🗂️ Estructura del Proyecto

```
CRUD-DJANGO-TAREAS/
├── djangocrud/          # Configuración principal de Django
│   ├── settings.py      # Configuraciones del proyecto
│   ├── urls.py          # URLs principales
│   └── wsgi.py          # Configuración WSGI
├── tasks/               # Aplicación principal
│   ├── models.py        # Modelo de datos Task
│   ├── views.py         # Lógica de negocio
│   ├── forms.py         # Formularios
│   ├── templates/       # Plantillas HTML
│   └── migrations/      # Migraciones de base de datos
├── manage.py            # Script de gestión de Django
└── db.sqlite3           # Base de datos SQLite
```

## 🎯 Funcionalidades Principales

### Modelo Task
- **title**: Título de la tarea (máximo 200 caracteres)
- **description**: Descripción opcional de la tarea
- **created**: Fecha y hora de creación (automática)
- **datecompleted**: Fecha de completado (opcional)
- **important**: Marca de importancia (booleano)
- **user**: Usuario propietario de la tarea

### Vistas Implementadas
- `home`: Página principal
- `registro_view`: Registro de usuarios
- `login_view`: Inicio de sesión
- `logout_view`: Cerrar sesión
- `create_Task`: Crear nueva tarea
- `listTasks`: Listar tareas pendientes
- `task_detaill`: Ver/editar tarea específica
- `task_complete`: Marcar tarea como completada
- `task_delete`: Eliminar tarea

## 🔧 Configuración

### Variables de Entorno
El proyecto utiliza configuraciones por defecto de Django. Para producción, considera configurar:

- `SECRET_KEY`: Clave secreta de Django
- `DEBUG`: Modo debug (False en producción)
- `DATABASE_URL`: URL de la base de datos

### Base de Datos
Por defecto usa SQLite. Para cambiar a PostgreSQL o MySQL:

1. Instala el driver correspondiente
2. Modifica `settings.py`
3. Ejecuta las migraciones

⭐ Si este proyecto te ayudó, ¡dale una estrella al repositorio! 
