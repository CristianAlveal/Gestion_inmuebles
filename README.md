# 🏠 Gestión de Inmuebles — Casas en Arriendo

Aplicación web desarrollada con **Django y Python** para la gestión de propiedades en arriendo. El sistema permite administrar inmuebles, usuarios y solicitudes de arriendo, diferenciando las funcionalidades disponibles según el rol de cada usuario.

El proyecto fue desarrollado como parte del proceso de aprendizaje y aplicación práctica de **Django, modelos, formularios, autenticación, grupos de usuarios, consultas ORM, templates y Bootstrap**.

---

## 📋 Descripción

**Casas en Arriendo** es una plataforma orientada a facilitar la publicación y administración de propiedades disponibles para arriendo.

La aplicación contempla diferentes tipos de usuarios:

- 👨‍💼 **Administrador:** administra usuarios e inmuebles y tiene acceso a las funciones administrativas.
- 🏠 **Arrendador:** puede registrar y administrar sus propios inmuebles y gestionar las solicitudes recibidas.
- 👤 **Arrendatario:** puede consultar los inmuebles disponibles y solicitar el arriendo de una propiedad.

El sistema permite mantener la información organizada y establecer un flujo básico entre arrendadores y arrendatarios.

---

## 🚀 Funcionalidades principales

### 👥 Gestión de usuarios

- Registro y administración de usuarios.
- Asociación de usuarios con perfiles mediante una relación `OneToOne`.
- Información personal:
  - Nombres.
  - Apellidos.
  - Teléfono.
  - Dirección.
  - Tipo de usuario.
- Edición de información personal.
- Gestión de `username` y correo electrónico.
- Autenticación mediante el sistema de usuarios de Django.
- Control de acceso mediante **Groups** de Django.

### 🔐 Roles y permisos

El sistema utiliza grupos para diferenciar las funcionalidades disponibles:

```text
Administrador
Arrendador
Arrendatario
```

Las vistas pueden restringir el acceso dependiendo del usuario autenticado y de su grupo.

Esto permite, por ejemplo:

- Restringir la creación de inmuebles a usuarios autorizados.
- Mostrar u ocultar opciones del menú según el rol.
- Permitir a los arrendadores administrar sus propias propiedades.
- Permitir a los arrendatarios realizar solicitudes de arriendo.

---

## 🏡 Gestión de inmuebles

Los inmuebles cuentan con información detallada como:

- Nombre.
- Descripción.
- Metros cuadrados construidos.
- Metros cuadrados totales.
- Número de estacionamientos.
- Número de habitaciones.
- Número de baños.
- Dirección.
- Comuna.
- Región.
- Tipo de inmueble.
- Precio mensual.
- Usuario propietario/arrendador.

### Tipos de inmueble

La aplicación contempla diferentes tipos de propiedades, entre ellos:

- Casa.
- Departamento.
- Parcela.

Los inmuebles pueden ser:

- ➕ Agregados.
- 👁️ Consultados.
- ✏️ Editados.
- 🗑️ Eliminados.

Los arrendadores pueden visualizar específicamente los inmuebles asociados a su usuario.

---

## 🇨🇱 Regiones y comunas de Chile

El proyecto incorpora una estructura para administrar:

```text
Región
   │
   └── Comuna
          │
          └── Inmueble
```

Se utiliza una relación entre regiones y comunas para facilitar la ubicación geográfica de los inmuebles.

La base de datos puede ser poblada mediante **fixtures JSON** utilizando:

```bash
python manage.py loaddata regiones_comunas.json
```

El proyecto contempla las **16 regiones y las comunas de Chile**.

---

## 📩 Solicitudes de arriendo

Una de las funcionalidades principales es el flujo de solicitud de arriendo.

Un arrendatario puede seleccionar un inmueble y enviar una solicitud.

El sistema permite manejar diferentes estados de una solicitud:

```text
PENDIENTE
ACEPTADA
RECHAZADA
```

El flujo general es:

```text
Arrendatario
      │
      ▼
Selecciona inmueble
      │
      ▼
Envía solicitud
      │
      ▼
Solicitud PENDIENTE
      │
      ▼
Arrendador revisa
      │
      ├──────────────┐
      ▼              ▼
  ACEPTADA        RECHAZADA
```

Además, se contempla que puedan existir múltiples solicitudes para un mismo inmueble, permitiendo al arrendador aceptar una solicitud o rechazarla.

---

## 🗃️ Modelos principales

La aplicación utiliza diferentes modelos relacionados entre sí.

Una estructura simplificada es:

```text
User
 │
 │ OneToOne
 ▼
Usuario
 │
 ├── tipo de usuario
 ├── nombres
 ├── apellidos
 ├── teléfono
 └── dirección
 │
 │
 └───────────────┐
                 │
                 ▼
             Inmueble
                 │
                 ├── Tipo_Inmueble
                 ├── Comuna
                 │      └── Región
                 │
                 └── Solicitudes
                         │
                         ▼
                     Arrendatario
```

---

## 🛠️ Tecnologías utilizadas

### Backend

- **Python**
- **Django**
- Django ORM
- Django Authentication
- Django Forms
- Django Groups
- Django Fixtures

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- Bootstrap Icons
- Templates de Django

### Base de datos

- PostgreSQL

### Herramientas

- Visual Studio Code
- Git
- GitHub
- pgAdmin

---

## 📄 Funcionalidades adicionales

El proyecto también incorpora diferentes funcionalidades para mejorar la experiencia de usuario:

- Diseño responsive mediante Bootstrap.
- Navbar con navegación entre las diferentes secciones.
- Menús dinámicos según el rol del usuario.
- Tablas para visualizar inmuebles.
- Formularios Bootstrap.
- Ventanas modales para determinadas acciones.
- Paginación de resultados.
- Validación de formularios.
- Mensajes de error y validación.
- Formateo de precios.
- Consultas mediante Django ORM.
- Ordenamiento de inmuebles.
- Generación de listados.
- Filtros por ubicación.
- Uso de `ForeignKey`, `OneToOneField` y relaciones entre modelos.

---

## 📊 Ejemplo de consulta ORM

Para obtener los inmuebles pertenecientes al usuario autenticado y ordenarlos desde el más reciente:

```python
inmuebles = request.user.inmuebles.all().order_by('-id')
```

También se utilizan consultas relacionadas para determinar, por ejemplo, si un inmueble posee solicitudes pendientes.

---

## 📁 Estructura general

Una estructura simplificada del proyecto es:

```text
proyecto_inmuebles/
│
├── manage.py
│
├── proyecto_inmuebles/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── gestion_inmuebles/
│   │
│   ├── models/
│   │   ├── inmueble.py
│   │   ├── usuario.py
│   │   ├── region.py
│   │   ├── comuna.py
│   │   └── ...
│   │
│   ├── controlador/
│   │   ├── inmuebleViews.py
│   │   ├── usuarioViews.py
│   │   └── ...
│   │
│   ├── templates/
│   │   ├── layout/
│   │   ├── inmuebles/
│   │   ├── usuarios/
│   │   └── ...
│   │
│   ├── forms.py
│   ├── urls.py
│   └── ...
│
└── fixtures/
    └── regiones_comunas.json
```

---

## ⚙️ Instalación

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresar al proyecto:

```bash
cd proyecto_inmuebles
```

Crear y activar el entorno virtual:

### Windows

```bash
python -m venv env
env\Scripts\activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Configurar la base de datos PostgreSQL en `settings.py`.

Ejecutar las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

Cargar los datos iniciales:

```bash
python manage.py loaddata regiones_comunas.json
```

Crear un superusuario:

```bash
python manage.py createsuperuser
```

Ejecutar el servidor:

```bash
python manage.py runserver
```

Luego acceder desde:

```text
http://127.0.0.1:8000/
```

---

## 🎯 Objetivo del proyecto

El objetivo principal del proyecto es desarrollar una aplicación web utilizando Django que permita aplicar conceptos fundamentales del desarrollo web backend, incluyendo:

- Arquitectura MVC/MVT.
- Modelado de datos.
- Relaciones entre modelos.
- Operaciones CRUD.
- Formularios Django.
- Autenticación.
- Autorización.
- Grupos y roles.
- Consultas ORM.
- Validación de información.
- Templates.
- Integración con Bootstrap.
- Persistencia de datos en PostgreSQL.

El proyecto representa la implementación progresiva de una plataforma de gestión de propiedades, incorporando funcionalidades de administración y un flujo de solicitudes de arriendo.

---

## 👨‍💻 Autor

**Cristian Alveal**

Proyecto desarrollado con fines académicos y de aprendizaje en desarrollo web utilizando Python y Django.
