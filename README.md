Kevin Millan

email: kmillanr@fractal-software.com

## Introducción
Este proyecto documenta el proceso de resolución del Desafío de Ingeniero de Datos. El desafío consiste en analizar un conjunto de datos de tweets para responder a consultas específicas, optimizando tanto el tiempo de ejecución como el uso de memoria.

## Consultas
1. Las 10 fechas con más tweets y el usuario con más tweets en esas fechas.
2. Los 10 emojis más usados y sus conteos.
3. Los 10 usuarios más influyentes basados en menciones.

Cada consulta tiene dos implementaciones: una optimizada para el tiempo de ejecución y la otra para el uso de memoria.

## Requisitos Previos

Para ejecutar este proyecto, necesitarás tener instalados los siguientes componentes:

- [Docker](https://www.docker.com/products/docker-desktop)

## Instrucciones para Ejecutar

### Paso 1: Clonar el Repositorio

Clona este repositorio en tu máquina local utilizando el siguiente comando:

```sh
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```
### Paso 2: Asegurarse de que el Archivo de Datos esté en el Directorio src
Asegúrate de que el archivo ```farmers-protest-tweets-2021-2-4.json``` esté en la carpeta ```root``` del proyecto.


### Paso 3: Construir la Imagen de Docker
Navega al directorio del proyecto y construye la imagen de Docker utilizando el archivo `Dockerfile` proporcionado:

```sh
docker build -t challenge_de_pyspark .
```

### Paso 4: Ejecutar el Contenedor de Docker
Ejecuta el contenedor de Docker con los puertos apropiados. Si los puertos 80 y 8888 están en uso, puedes utilizar puertos alternativos como se muestra a continuación:

```sh
docker run -p 8080:80 -p 8890:8888 challenge_de_pyspark
```

### Paso 5: Acceder a los Servicios
#### Jupyter Notebook
Abre tu navegador web y navega a http://localhost:8890 para acceder a Jupyter Notebook. Aquí podrás ejecutar y revisar el notebook data_processing_with_pyspark.ipynb que contiene la implementación y análisis de las consultas.

#### Aplicación Flask
Puedes acceder a la aplicación Flask navegando a http://localhost:8080/run o utilizando curl:

```sh
curl -X GET "http://localhost:8080/run"
```

Esto ejecutará las funciones de análisis y mostrará los resultados.

## Estructura del Proyecto

* src/: Contiene los archivos Python con las implementaciones de las consultas.
* q1_time.py: Implementación optimizada para el tiempo de ejecución de la primera consulta.
* q1_memory.py: Implementación optimizada para el uso de memoria de la primera consulta.
* q2_time.py: Implementación optimizada para el tiempo de ejecución de la segunda consulta.
* q2_memory.py: Implementación optimizada para el uso de memoria de la segunda consulta.
* q3_time.py: Implementación optimizada para el tiempo de ejecución de la tercera consulta.
* q3_memory.py: Implementación optimizada para el uso de memoria de la tercera consulta.
* data_processing_with_pyspark.ipynb: Notebook de Jupyter con la documentación y ejecución de las consultas.
* Dockerfile: Archivo de configuración para construir la imagen de Docker.
* uwsgi.ini: Archivo de configuración de uWSGI para ejecutar la aplicación Flask.
* requirements.txt: Archivo con las dependencias de Python necesarias para el proyecto.

### Notas
Asegúrate de reemplazar "farmers-protest-tweets-2021-2-4.json.json" en el notebook de Jupyter con la ruta correcta a tu archivo JSON de tweets.
Si encuentras algún problema, revisa los logs del contenedor de Docker para obtener más detalles.



## Sugerencias para Optimizar el Proceso

1. **Uso de Caché**: Implementar un mecanismo de caché para almacenar los resultados de consultas frecuentes. Esto puede reducir significativamente el tiempo de ejecución para consultas repetitivas.

2. **Procesamiento en Paralelo**: Utilizar bibliotecas de procesamiento en paralelo como `multiprocessing` en Python para dividir y procesar los datos en múltiples núcleos de CPU.

3. **Optimización de Consultas Spark**: Aprovechar las optimizaciones de Spark, como persistencia y particionamiento, para manejar grandes volúmenes de datos de manera más eficiente.

4. **Uso de Columnar Storage Formats**: Convertir los datos a formatos de almacenamiento columnar como Parquet o ORC, que son más eficientes para consultas analíticas.

5. **Indexación**: Crear índices en los campos más consultados para acelerar las consultas de búsqueda y filtrado.

6. **Reducción de Datos**: Filtrar y limpiar los datos antes de realizar análisis complejos para reducir la cantidad de datos a procesar.

7. **Optimización de Memoria**: Utilizar estructuras de datos más eficientes en memoria, como `numpy` y `pandas`, y liberar memoria innecesaria durante el procesamiento.

8. **Monitoreo y Perfilado**: Implementar herramientas de monitoreo y perfilado para identificar cuellos de botella en el rendimiento y optimizar el código en consecuencia.