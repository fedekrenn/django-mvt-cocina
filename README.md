# 👨‍🍳 Recetas de cocina — Django (MVT)

Proyecto de ejemplo para gestionar recetas, cocineros, restaurantes y proveedores. Incluye registro/login de usuarios, CRUD para los modelos principales y un buscador de recetas.

## Contenido

- Resumen del proyecto
- Requisitos
- Instalación (entorno virtual y dependencias)
- Configuración de la base de datos y migraciones
- Uso (ejecución local)
- Solución de problemas comunes
- Contribuir

---

## Resumen

Esta web permite:

- Visualizar y buscar recetas (público)
- Registro y login de usuarios
- CRUD sobre Recetas, Cocineros, Restaurantes y Proveedores (usuarios autenticados)
- Gestión de avatar por usuario

Modelos principales: `Receta`, `Cocinero`, `Restaurante`, `Proveedor`, `Avatar`.

---

## Requisitos

- Python 3.11–3.13 (recomendado: 3.12 para máxima compatibilidad)
- MySQL o SQLite (para desarrollo rápido) — ver sección de configuración
- Git
- pip

Nota: Si usas Python 3.13 puedes necesitar versiones actualizadas de paquetes (Pillow, pyzmq, etc.). El `requirements.txt` del proyecto ya contiene versiones compatibles probadas con Python 3.13.

---

## Instalación (desarrollo)

1. Clonar el repositorio:

```bash
git clone https://github.com/fedekrenn/django-mvt-cocina.git
cd django-mvt-cocina
```

2. Crear y activar un entorno virtual

```bash
python -m venv env_cocinando
```

3. Activar el entorno virtual:

```bash
env_cocinando\Scripts\Activate
```

4. Actualizar pip y herramientas de construcción (importante en Windows):

```bash
python -m pip install --upgrade pip setuptools wheel
```

5. Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Migraciones y superusuario

Después de configurar la DB, aplica migraciones y crea un superusuario:

```bash
python manage.py migrate
python manage.py createsuperuser
```

---

## Ejecutar en desarrollo

```bash
python manage.py runserver
# Visitar http://127.0.0.1:8000/
```

Para cargar archivos estáticos (cuando sea necesario):

```bash
python manage.py collectstatic
```

---

## Variables de entorno (.env)

Para mantener fuera del repositorio la información sensible (credenciales de BD, secret key, debug), puedes usar un archivo `.env` en la raíz del proyecto.

1. Crea el archivo copiando el ejemplo:

```bash
cp .env.example .env
# o en Windows PowerShell
Copy-Item .env.example .env
```

2. Edita `.env` y reemplaza los valores por tus credenciales.

3. `proyecto_final/settings.py` ya carga variables desde `.env` mediante `python-dotenv`.

Variables disponibles (ejemplo en `.env.example`):

- `DJANGO_SECRET_KEY` — clave secreta de Django
- `DJANGO_DEBUG` — `True`/`False` (controla DEBUG)
- `DJANGO_DB_ENGINE` — engine DB (`django.db.backends.sqlite3` o `mysql.connector.django`)
- `DJANGO_DB_NAME`
- `DJANGO_DB_USER`
- `DJANGO_DB_PASSWORD`
- `DJANGO_DB_HOST`
- `DJANGO_DB_PORT`

Después de crear `.env`, procede con `python manage.py migrate` normalmente.

---

## Funcionalidades clave

- Buscar recetas desde la página principal (formulario en `aplicacion/templates/aplicacion/index.html`).
- CRUD completo para modelos principales (requiere autenticación).
- Gestión de avatar por usuario.

## Capturas / Videos

Primera pantalla (lista de recetas):

![Lista de recetas](https://github.com/fedekrenn/Krenn-Federico-Comision-43865/assets/90353038/725bccd0-a1b7-4242-ae33-9da9b1652081)

Pantalla de usuario / perfil:

![Perfil y nav](https://github.com/fedekrenn/Krenn-Federico-Comision-43865/assets/90353038/b4573eb1-45b1-49a8-adf6-f7fbde1f08ca)

Gestión de avatar en el perfil del usuario:

![Avatar usuario](https://github.com/fedekrenn/Krenn-Federico-Comision-43865/assets/90353038/114fd26f-18fa-4c13-af4e-c718d5ce8205)

Modal de carga / registro de elementos (ej. recetas):

![Modal de carga](https://github.com/fedekrenn/Krenn-Federico-Comision-43865/assets/90353038/41a82d4c-0249-4a67-8643-0b583dac0fd4)

Acciones (detalle / editar / eliminar) en las tablas:

![Acciones en tabla](https://github.com/fedekrenn/Krenn-Federico-Comision-43865/assets/90353038/c3a99878-447d-40ca-9dde-ff9c4c5b5dd0)

Acceso al panel de administrador (superuser):

![Panel admin](https://github.com/fedekrenn/Krenn-Federico-Comision-43865/assets/90353038/3007e6b4-4b11-4147-be14-34f311cb716d)

---

## Pruebas y verificación rápida

Actualmente el proyecto no incluye una suite extensa de tests automatizados. Para una comprobación manual básica:

1. Ejecuta `python manage.py migrate`.
2. Crea un superuser: `python manage.py createsuperuser`.
3. Levanta el servidor y prueba las rutas principales.

---

## Contribuir

1. Haz fork del repositorio.
2. Crea una rama para tu feature/bugfix: `git checkout -b feature/nombre`.
3. Haz commits claros y push.
4. Abre un Pull Request describiendo el cambio.

Antes de aportar, prueba localmente las migraciones y las vistas que modifiques.

---

<br>

## 🙋‍♂️ Hola, Soy Federico Krenn

:nerd_face: Software Developer
<br>
👨‍🎓 Técnico Superior en Desarrollo Web y aplicaciones. También me encuentro realizando la Tecnicatura en Software Libre en la UNL.
<br>
📫 Conectemos en Linkedin: https://www.linkedin.com/in/fkrenn/