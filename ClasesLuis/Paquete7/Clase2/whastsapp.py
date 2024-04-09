from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

# Inicia una instancia del navegador Chrome
driver = webdriver.Chrome()

# Abre WhatsApp Web en el navegador
driver.get('https://web.whatsapp.com/')
input('Escanea el código QR y presiona Enter para continuar...')

# Nombre de la conversación donde está el audio
nombre_conversacion = "Alex GM"

# Encuentra la conversación
search_box = driver.find_element('xpath', '//div[@class="_3FRCZ copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"]')
search_box.send_keys(nombre_conversacion)
time.sleep(2)  # Espera 2 segundos para que se carguen los resultados de búsqueda

# Abre la conversación
conversation = driver.find_element_by_xpath(f'//span[@title="{nombre_conversacion}"]')
conversation.click()

# Espera a que se carguen los mensajes
time.sleep(2)

# Encuentra y haz clic en el primer audio en la conversación
audio_element = driver.find_element_by_xpath('//div[@class="_3WjMU DcB6W"]')
audio_element.click()

# Espera a que se reproduzca el audio
time.sleep(5)  # Puedes ajustar el tiempo de espera según sea necesario

# Descarga el audio utilizando la combinación de teclas Ctrl+S (Windows) o Cmd+S (Mac)
#pyautogui.hotkey('ctrl', 's')  # Para Windows
pyautogui.hotkey('command', 's')  # Para Mac

# Espera un momento para que aparezca el cuadro de diálogo "Guardar como"
time.sleep(2)

# Ingresa el nombre del archivo y presiona Enter para guardar
pyautogui.typewrite('audio_whatsapp')
pyautogui.press('enter')

# Cierra el navegador
driver.quit()
