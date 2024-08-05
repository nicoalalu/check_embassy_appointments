# Proyecto de Scraping de Turnos en la Embajada de España

Este proyecto tiene como objetivo scrapear la página de la Embajada de España para verificar si hay nuevos turnos abiertos para renovar el pasaporte. Si se encuentran nuevos turnos disponibles, recibirás una notificación a través de Telegram con la fecha y el enlace para inscribirse.

## Requisitos

- Python 3.7 o superior
- Cuenta de Telegram
- Token de bot de Telegram
- Cuenta en Google Cloud Platform (GCP)

## Instalación
    
## Configuración

1. **Crear un bot en Telegram:**

    - Abre Telegram y busca el usuario `@BotFather`.
    - Inicia una conversación y usa el comando `/newbot` para crear un nuevo bot.
    - Sigue las instrucciones para nombrar tu bot y obtener el token de API.
    - Guarda el token de API para más tarde.
    - Abre telegram web y dirigite al grupo donde alojarás al bot. Copia del link los números luego del #. Ese sera tu CHAT_ID

2. **Configurar el proyecto:**

    - Crea un archivo `config.ini` en la raíz del proyecto y agrega las siguientes variables:

        ```ini
      [telegram]

      BOT_TOKEN=6301804665:AAGZy4YAjuFZzbSF58rkGnPtd6dC151NE2M
      CHAT_ID=-4137652059
        ```

3. **Configurar Google Cloud Platform:**

    - Crea un proyecto en Google Cloud Platform.
    - Habilita las APIs de Cloud Functions y Cloud Scheduler.
    - Instala la herramienta de línea de comandos de Google Cloud SDK si aún no la tienes.
    - Autentica tu cuenta con `gcloud auth login`.
    - Configura el proyecto con `gcloud config set project [YOUR_PROJECT_ID]`.

## Implementación en Google Cloud Platform

1. **Crear la Cloud Function:**

    - Sube el .py a la raíz del proyecto

    - Crea un archivo `requirements.txt` en la raíz del proyecto con el siguiente contenido:

        ```plaintext
    requests
    beautifulsoup4
    telebot
    configparser

        ```

    - Despliega la Cloud Function:

        ```powershell
        gcloud functions deploy check_appointments --runtime python39 --trigger-http --allow-unauthenticated
        ```

2. **Configurar Cloud Scheduler:**

    - Ve a la consola de Google Cloud Platform.
    - Navega a Cloud Scheduler y crea un nuevo job.
    - Configura el job para que se ejecute diariamente (o según la frecuencia deseada).
    - En el campo URL, ingresa el endpoint HTTP de tu Cloud Function.
    - En el campo HTTP method, selecciona `POST`.
    - Guarda el job.

## Uso

La Cloud Function se ejecutará automáticamente según la programación configurada en Cloud Scheduler. Cuando se encuentren nuevos turnos disponibles, recibirás una notificación en Telegram.
