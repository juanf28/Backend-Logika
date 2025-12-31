# Logika Backend Test

## Descripción

API desarrollada en **FastAPI** para la gestión de usuarios y tareas (CRUD).
Incluye autenticación mediante **JWT**, manejo de base de datos con **PostgreSQL en Docker**,
migraciones con **Alembic** y seguridad de contraseñas usando **bcrypt**.

## Tecnologías

- Python 3.11.8
- FastAPI
- SQLAlchemy
- PostgreSQL (en Docker)
- Alembic (migraciones)
- Passlib (hash de contraseñas)
- JWT (autenticación)
- Uvicorn (servidor ASGI)
- Docker & Docker Compose

---

## Requisitos

- Python 3.11.8
- Git
- Docker
- Docker Compose
- Entorno virtual (venv)

---

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/juanf28/Backend-Logika.git
cd logika-backend

2. Crear y activar entorno virtual
python -m venv venv

venv\Scripts\activate

3. Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

4. Configurar variables de entorno

Crear un archivo .env en la raíz del proyecto con el siguiente contenido:

DATABASE_URL=postgresql://postgres:postgres@localhost:5432/logika
SECRET_KEY=super_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30

5. Levantar la base de datos con Docker

La base de datos PostgreSQL se ejecuta localmente usando Docker Compose.

docker compose up -d


Este comando levanta un contenedor con PostgreSQL y crea automáticamente la base de datos logika.

6. Ejecutar migraciones
alembic upgrade head


Este comando crea todas las tablas necesarias en la base de datos.

7. Ejecutar la aplicación
uvicorn app.main:app --reload


La API estará disponible en:

http://127.0.0.1:8000

Documentación de la API

Swagger se utiliza únicamente como herramienta de documentación y prueba. Tambien funciona con postman o otro cliente http

Swagger UI:

http://127.0.0.1:8000/docs

Funcionalidades principales

Registro de usuarios

Login con autenticación JWT

Endpoints protegidos

CRUD de tareas

Paginación

Manejo de errores

Migraciones de base de datos con Alembic

Seguridad

Contraseñas encriptadas con bcrypt

Autenticación basada en JWT

Protección de endpoints mediante dependencias de FastAPI

Notas adicionales

La base de datos solo se ejecuta de forma local mediante Docker.

La API puede ser consumida desde cualquier cliente HTTP como Postman, Curl o aplicaciones frontend.