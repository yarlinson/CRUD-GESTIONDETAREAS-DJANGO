# 📋 Task Manager - Django & REST API

Una aplicación web moderna para la gestión de tareas, construida con Django y REST Framework. Combina una interfaz web intuitiva con una API REST completamente documentada.

![Django](https://img.shields.io/badge/Django-5.2-green.svg)
![DRF](https://img.shields.io/badge/DRF-3.14-red.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Características

### 🌐 Interfaz Web
- Sistema completo de autenticación (registro, login, logout)
- Gestión de tareas (crear, editar, eliminar)
- Marcado de tareas como completadas
- Filtrado por estado (pendientes/completadas)
- Interfaz responsive con Bootstrap
- Protección CSRF y validación de formularios

### 🔌 API REST
- Documentación completa con Swagger/OpenAPI
- Autenticación basada en tokens
- CRUD completo para tareas
- Filtrado y búsqueda avanzada
- Paginación automática
- Endpoints específicos para tareas completadas/pendientes

## 🛠️ Tecnologías

- **Backend**
  - Django 5.2
  - Django REST Framework
  - drf-yasg (Swagger/OpenAPI)
  
- **Frontend**
  - Bootstrap 5
  - HTML5 & CSS3
  - JavaScript
  
- **Base de Datos**
  - SQLite
  
- **Autenticación**
  - Token-based Authentication
  - Django Authentication

## 📦 Instalación

1. **Clonar el repositorio**
```bash
git clone <tu-repositorio>
cd CRUD-DJANGO-TAREAS
```

2. **Crear y activar entorno virtual**
```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install django djangorestframework drf-yasg django-widget-tweaks
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

## 🔌 API Endpoints

### Autenticación
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/token/` | Obtener token de autenticación |

### Tareas
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/tasks/` | Listar todas las tareas |
| POST | `/api/tasks/` | Crear nueva tarea |
| GET | `/api/tasks/{id}/` | Ver detalle de tarea |
| PUT | `/api/tasks/{id}/` | Actualizar tarea |
| DELETE | `/api/tasks/{id}/` | Eliminar tarea |
| POST | `/api/tasks/{id}/complete/` | Marcar como completada |
| GET | `/api/tasks/completed/` | Listar tareas completadas |
| GET | `/api/tasks/pending/` | Listar tareas pendientes |

### Documentación
| Endpoint | Descripción |
|----------|-------------|
| `/swagger/` | UI interactiva de Swagger |
| `/redoc/` | Documentación con ReDoc |

## 🚀 Uso de la API

### Obtener Token
```bash
curl -X POST http://localhost:8000/api/token/ \
  -d "username=tuusuario&password=tucontraseña"
```

### Usar Token
```bash
curl -H "Authorization: Token tutoken" \
  http://localhost:8000/api/tasks/
```

## 🔍 Características de la API

### Filtrado y Búsqueda
- Búsqueda por título y descripción
- Ordenamiento por:
  - Fecha de creación
  - Fecha de completado
  - Importancia
- Paginación (10 items por página)

### Seguridad
- Autenticación requerida
- Protección CSRF
- Validación de datos
- Aislamiento por usuario

## 📁 Estructura del Proyecto

```
CRUD-DJANGO-TAREAS/
├── djangocrud/          # Configuración principal
├── tasks/              # Aplicación principal
│   ├── api.py         # Vistas de la API
│   ├── models.py      # Modelos de datos
│   ├── serializers.py # Serializadores
│   ├── views.py       # Vistas web
│   └── templates/     # Plantillas HTML
└── manage.py
```

## 🤝 Contribuir

1. Fork el repositorio
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: Nueva característica'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request


## 👤 Autor

**Yarlinson Tiberio Barranco Bastilla**

- GitHub: [@yarlinson](https://github.com/yarlinson)

---
⭐️ ¡Si te gusta el proyecto, dale una estrella! ⭐️
