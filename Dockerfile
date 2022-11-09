# Especficar la imagen base
FROM python:3.10

# Instalar las dependencias necesarias
RUN pip install pandas

# Definir el working directory
WORKDIR /app

# Copiar el script local que acabamos de crear al working directory
COPY . /app

# Definir un entrypoin
ENTRYPOINT ["python", "main.py"]