@echo off
REM Activar el entorno virtual
call .\env\Scripts\activate

REM Realizar makemigrations
python manage.py makemigrations

REM Realizar migrate
python manage.py migrate

REM Iniciar el servidor de desarrollo
python manage.py runserver