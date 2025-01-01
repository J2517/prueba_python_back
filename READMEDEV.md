# Informe JSONPlaceholder API Integration

*1. Introducción*

Este proyecto es una integración con la API pública de JSONPlaceholder, que ofrece datos simulados. La aplicación utiliza **FastAPI** como framework principal y proporciona endpoints para consultar información de usuarios, publicaciones y timestamps, además, se integra el manejo y almacenamiento de logs.

*2. Objetivos*

* Implementar una API funcional usando FastAPI
* Consumir y procesar datos de JSONPlaceholder
* Implementar logging y manejo de errores.
* Implementar pruebas unitarias 


*3. Arquitectura*

API REST simplificada, diseñada como una solución ligera para cumplir con los requerimientos básicos del ejercicio. 

*4. Respuesta a requerimientos*
* Un endpoint */users/{id}*:
Se realizó un método asíncorono llamado *get_user* que obtiene la información de un usuario. El método recibe un parámetro *user_id*, realiza una solicitud GET al endpoint correspondiente de la API para obtener los datos del usuario. Si la solicitud es exitosa, se almacena la información obtenida a través del método *set_last_user*, y se retorna un diccionario que incluye la fecha y hora actual junto con los datos del usuario.
* Un endpoint */posts*:
Se realizó un método asíncrono llamado *get_posts* que tiene como objetivo obtener las publicaciones asociadas al último usuario consultado. Primero, verifica si existe un usuario previamente consultado mediante la función *has_user* de *user_state*; si no es así, lanza una excepción que indica que se debe consultar primero un usuario a través del endpoint */users/{id}*. Si se encuentra un usuario, se obtiene su ID y se realiza una solicitud GET a la API para obtener las publicaciones de ese usuario. Si la respuesta es exitosa, se retorna un diccionario que incluye la fecha y hora actual, el id del usuario consultado, las publicaciones y el conteo de éstas.
* Fecha y hora
Se realizó un método asíncrono llamado *get_current_datetime* que tiliza la función datetime.now() para obtener la fecha y hora del sistema en el momento de la ejecución, y luego utiliza el método strftime para formatear la fecha y hora en el formato deseado.
* Logs
Se estableció una configuración global en *main.py* que proporciona la configuración del sistema de registros y los almacena en el archivo *app.log*

*5. Como ejecutar la aplicación*
* Instale las dependencias con el comando *pip install -r requirements.txt*
* Inicie el servidor con el comando *uvicorn main:app --reload*
* Ingrese al enlace *http://127.0.0.1:8000/docs*

*6. Como realizar las pruebas
* Utilice el comando *python -m pytest*