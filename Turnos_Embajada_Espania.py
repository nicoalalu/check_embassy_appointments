import requests
from bs4 import BeautifulSoup
import configparser
import telebot
import requests
from datetime import datetime

url = 'https://www.cgeonline.com.ar/informacion/apertura-de-citas.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.content)

proxima_apertura = soup.small.find_next().find_next().contents[0]

if proxima_apertura.startswith(tuple('0123456789')):

    proxima_apertura_date = datetime.strptime(proxima_apertura[0:10], "%d/%m/%Y")

    if proxima_apertura_date > datetime.now():
        config = configparser.ConfigParser()
        config.read('config.ini')
        token = config['telegram']['BOT_TOKEN']
        chat_id = "-4137652059"
        message = "📣❗Se ha abierto una nueva fecha para tramitar tu pasaporte 🇪🇸 para el " + proxima_apertura + ". Saca tu turno en https://www.cgeonline.com.ar/tramites/citas/opciones-pasaporte.html"
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url).json()) # this sends the message
    else:
        print("No hay turnos disponibles")

else:
    print(proxima_apertura)

