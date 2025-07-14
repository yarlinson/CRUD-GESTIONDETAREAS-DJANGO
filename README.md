# 📋 CRUD Django - Sistema de Gestión de Tareas

Un sistema completo de gestión de tareas desarrollado con Django que permite a los usuarios crear, gestionar y organizar sus tareas personales. Este proyecto implementa operaciones CRUD (Create, Read, Update, Delete) con autenticación de usuarios y una interfaz moderna usando Tailwind CSS.

## ✨ Características Principales

- 🔐 **Sistema de Autenticación**
  - Registro de usuarios con encriptación de contraseñas
  - Login y logout seguros
  - Protección de rutas con decorador @login_required

- 📝 **Gestión Completa de Tareas**
  - Crear nuevas tareas con título y descripción
  - Ver lista de tareas pendientes
  - Editar tareas existentes
  - Eliminar tareas no necesarias
  - Marcar/Desmarcar tareas como completadas
  - Registro automático de fecha de creación y completado

- 🎨 **Interfaz Moderna**
  - Diseño responsive con Tailwind CSS
  - Formularios estilizados y validados
  - Feedback visual para acciones del usuario
  - Confirmación para acciones importantes

- 🔒 **Seguridad y Privacidad**
  - Cada usuario solo puede ver y gestionar sus propias tareas
  - Validación de permisos en cada operación
  - Protección CSRF en formularios
  - Manejo seguro de sesiones

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 5.2
- **Frontend**: Tailwind CSS
- **Base de Datos**: SQLite3
- **Autenticación**: Django Auth System
- **Formularios**: Django Forms + Widget Tweaks

## 📋 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Navegador web moderno

## 🚀 Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/CRUD-DJANGO-TAREAS.git
   cd CRUD-DJANGO-TAREAS
   ```

2. **Crear y activar entorno virtual**
   ```bash
   python -m venv venv

   # Windows:
   venv\Scripts\activate

   # Linux/macOS:
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar migraciones**
   ```bash
   python manage.py migrate
   ```

5. **Crear superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Iniciar servidor**
   ```bash
   python manage.py runserver
   ```

## 📱 Uso del Sistema

### Rutas Principales
- `/`: Página de inicio
- `/registro/`: Crear nueva cuenta
- `/login/`: Iniciar sesión
- `/tasks/create/`: Crear y gestionar tareas
- `/tasks/`: Ver lista de tareas pendientes

### Gestión de Tareas
1. Inicia sesión o regístrate
2. Ve a `/tasks/create/` para:
   - Crear nuevas tareas
   - Ver tus tareas existentes
   - Marcar/desmarcar tareas como completadas
   - Editar o eliminar tareas

## 🗂️ Estructura del Proyecto

```
CRUD-DJANGO-TAREAS/
├── djangocrud/          # Configuración del proyecto
│   ├── settings.py      # Configuraciones
│   ├── urls.py          # URLs principales
│   └── wsgi.py          # Configuración WSGI
├── tasks/               # Aplicación de tareas
│   ├── models.py        # Modelo Task
│   ├── views.py         # Lógica de negocio
│   ├── forms.py         # Formularios
│   └── templates/       # Plantillas HTML
└── manage.py           # Script de Django
```

## 📦 Modelo de Datos

### Task
- `title`: CharField(200) - Título de la tarea
- `description`: CharField - Descripción (opcional)
- `created`: DateTimeField - Fecha de creación (automática)
- `datecompleted`: DateTimeField - Fecha de completado (opcional)
- `important`: BooleanField - Marca de importancia
- `user`: ForeignKey - Usuario propietario

## 🔄 Funcionalidades Implementadas

### Vistas
- `home`: Página principal
- `registro_view`: Registro de usuarios
- `login_view`: Autenticación
- `create_Task`: Crear y listar tareas
- `task_detaill`: Editar tarea
- `task_complete`: Marcar/desmarcar completada
- `task_delete`: Eliminar tarea

## 🤝 Contribuir

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Agrega nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

