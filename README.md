###Backend

Dentro del ambiente virtual env correr la siguiente linea para instalar todas las dependencias:

pip install -r requirements.txt

Crear la base de datos y crear un archivo .env en donde se indique la secret key del proyecto

SECRET_KEY=''

luego ingresar en la carpeta backend y ejecutar el comando:

py manage.py runserver

###Frontend

Dentro de la carpeta frontend ejecutar el comando:

npm install

Para correr el proyecto ejecutar:

npm run dev