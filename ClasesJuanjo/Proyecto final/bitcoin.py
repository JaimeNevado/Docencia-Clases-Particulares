import requests
import json
import time

# URL de la API de CoinGecko para obtener el precio de Bitcoin en USD
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

# Nombre del archivo de texto donde se escribirá el precio de Bitcoin
archivo_txt = "precio_bitcoin.txt"

while True:
    try:
        # Realizar una solicitud GET a la API de CoinGecko
        response = requests.get(url)
        
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            data = response.json()
            
            # Obtener el precio de Bitcoin en USD
            precio_bitcoin = data["bitcoin"]["usd"]
            
            # Guardar el precio en el archivo de texto
            with open(archivo_txt, "w") as file:
                file.write(f"Precio de Bitcoin en USD: {precio_bitcoin}")
                
            print(f"Precio de Bitcoin en USD: {precio_bitcoin}USDT")
        
        else:
            print(f"No se pudo obtener el precio. Código de estado: {response.status_code}")
    
    except Exception as e:
        print(f"Error: {e}")
    
    # Esperar un período de tiempo antes de volver a consultar el precio (por ejemplo, cada 60 segundos)
    time.sleep(60)
