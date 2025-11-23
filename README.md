# Seguridad Arauco — Sistema de Registro de Visitas y Checklists  
Proyecto académico — Programación Backend — INACAP  

Este proyecto es un sistema web desarrollado con **Python + Django + MariaDB**, enfocado en el **registro de visitas de seguridad y checklists operacionales** en el contexto de la empresa forestal **Arauco**.

El objetivo es permitir que supervisores registren visitas en terreno, generen checklists asociados, gestionen estados y mantengan trazabilidad operativa. Incluye autenticación, CRUD completo, logs, admin panel y pruebas automatizadas.

---

# 1. Tecnologías utilizadas
- **Python 3.12+**
- **Django 5.2**
- **MariaDB 10+ / MySQL compatible**
- **mysqlclient** (conector)
- **HTML + Bootstrap**
- **Autenticación estándar de Django**
- **Logs con logging**
- **Tests automatizados**

---

# 2. Estructura del proyecto

```
SeguridadArauco/
│── seguridad_arauco/      # Configuración general del proyecto
│── visitas/               # App principal (CRUD visitas + checklists)
│   ├── migrations/
│   ├── templates/
│   ├── fixtures/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│── usuarios/              # App de login (si corresponde)
│── .env                   # Variables de entorno
│── requirements.txt      
│── README.md
```

---

# 3. Variables de entorno (.env)

Debe estar en la raíz del proyecto:

```
DB_NAME=arauco_seguridad
DB_USER=root
DB_PASSWORD=admin
DB_HOST=127.0.0.1
DB_PORT=3306

SECRET_KEY=tu_key_unica
DEBUG=True
```

---

# 4. Instalación del proyecto (PASO A PASO)

## Paso 1 — Clonar proyecto o descomprimir carpeta

```
git clone https://github.com/CristianAlejandroMunoz/SeguridadArauco.git
cd SeguridadArauco
```

---

## Paso 2 — Crear entorno virtual

```
python -m venv .venv
```

Activarlo:

### En Windows:
```
.venv\Scripts\activate
```

### En Linux/Mac:
```
source .venv/bin/activate
```

---

## Paso 3 — Instalar dependencias

```
pip install -r requirements.txt
```

---

## Paso 4 — Configurar la base de datos MariaDB

Entrar al cliente MariaDB:

```
mariadb -u root -p
```

Crear base:

```sql
CREATE DATABASE arauco_seguridad CHARACTER SET utf8mb4;
```

---

## Paso 5 — Aplicar migraciones

```
python manage.py makemigrations
python manage.py migrate
```

---

## Paso 6 — Crear superusuario

```
python manage.py createsuperuser
```

Recomendación para pruebas:

- Usuario: admin  
- Correo: admin@administrador.com  
- Contraseña: admin

---

## Paso 7 — Cargar datos de prueba (fixtures)

```
python manage.py loaddata visitas.json
python manage.py loaddata checklist.json
```

Los archivos están en:

```
visitas/fixtures/
```

---

## Paso 8 — Ejecutar el servidor

```
python manage.py runserver
```

Luego abrir el navegador en:

```
http://127.0.0.1:8000/
```

---

# 5. Funcionalidades Principales

## Registro de visitas  
- Crear visita  
- Editar visita  
- Ver detalle  
- Eliminar visita  
- Listado completo  

## Checklist por visita  
- Crear checklist asociado  
- Editar checklist  
- Eliminar checklist  

## Autenticación  
- Login / Logout  
- Protección con LoginRequired  
- Panel de administración  

## Admin panel avanzado  
```
http://127.0.0.1:8000/admin/
```

---

# 6. Pruebas automatizadas

Para ejecutar los tests:

```
python manage.py test visitas
```

¿Qué hace?

- Crea una base temporal `test_arauco_seguridad`
- Ejecuta los tests del CRUD
- Elimina la base temporal

---

# 7. Comandos principales y su explicación

| Comando | Explicación |
|--------|-------------|
| `python manage.py makemigrations` | Detecta cambios en modelos y genera archivos de migración |
| `python manage.py migrate` | Aplica migraciones a la BD real |
| `python manage.py runserver` | Inicia el servidor web Django |
| `python manage.py test` | Ejecuta pruebas unitarias |
| `python manage.py createsuperuser` | Crea un usuario admin |
| `pip install -r requirements.txt` | Instala todas las dependencias del proyecto |
| `loaddata archivo.json` | Carga datos desde un fixture |

---

# 8. Lista de dependencias (archivo requirements.txt)

Incluye:

- Django
- mysqlclient
- python-dotenv
- pymysql (para compatibilidad)
- tzdata

Este archivo se incluye abajo y debe ir en la raíz del proyecto.

---

# 9. Autor

Proyecto desarrollado para la asignatura:  
**Programación Backend — INACAP**  
Evaluación Unidad 03  
Estudiante: *Cristian Muñoz Mora*

---

# 10. Objetivo educativo

Este proyecto cumple los requisitos de la rúbrica:

- Autenticación  
- CRUD completo  
- Conexión a BD  
- Uso de fixtures  
- Tests unitarios  
- Manejo de errores  
- Logging  
- Buenas prácticas de código  
- Documentación profesional  

