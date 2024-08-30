# Utilizamos una imagen base de Python
FROM python:3.9-slim-buster

# Establecemos el directorio de trabajo
WORKDIR /api_spotify_connection

# Copiamos el código de nuestra aplicación al contenedor
COPY . .

# Instalamos las dependencias (si las hubiera)
# RUN pip install -r requirements.txt
RUN pip install -r requirements.txt

# Exponemos el puerto 8080
#EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "./songsbyspotify.py"]







