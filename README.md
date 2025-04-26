# School_Management_Authentication_System

## Project Setup
- First create a virtual environment `env` and activate it.
```bash
python3 -m venv env
source env/bin/activate
```
- Install Django and Django REST Framework
```bash
pip install django djangorestframework
```
- Add a `requirements.txt` file
```bash
pip freeze > requirements.txt
```
- Create a Django Project at the root directory
```bash
django-admin startproject school_management_auth_system .
```
- Create an `apps` package where all the app modules will be kept
- Install psycopg2 for PostgreSQL which is the PostgreSQL adapter for Python. This is what Django will use to connect to PostgreSQL.
```bash
pip install psycopg2
```
- Create database
    - Enter into postgreSQL
    ```bash
    sudo -u postgres psql
    ```
    - Create a database, user and grant user to the database
    ```sql
    CREATE DATABASE school_management_auth_system_db;
    CREATE USER school_management_auth_system_user WITH PASSWORD 'password';
    GRANT ALL PRIVILEGES ON DATABASE school_management_auth_system_db TO school_management_auth_system_user;
    ```
- Update Django Settings to Use PostgreSQL in our `school_management_auth_system/settings.py`
```py
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'school_management_auth_system_db',
        'USER': 'school_management_auth_system_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',  # or your database host
        'PORT': '5432',       # default port for PostgreSQL
    }
}
```
- Run migration
```bash
python3 manage.py migrate
```
- Run the runserver
```bash
python3 manage.py runserver
```

## Add Simple-Jwt Authentication
- Install simple jwt
- Congfigure `simple-jwt` in django settings
