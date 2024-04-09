from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Inicializar el navegador (asegúrate de tener el controlador adecuado instalado y configurado)
driver = webdriver.Chrome()  # Puedes cambiar 'Chrome' por 'Firefox' si lo prefieres

# Abrir WhatsApp Web
driver.get('https://web.whatsapp.com/')


# Enviar mensaje a un contacto/grupo
contacto_nombre = "Alex GM"
mensaje = "¡Hola desde Python!"

# Buscar el campo de búsqueda y escribir el nombre del contacto/grupo
search_box = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
search_box.click()
search_box.send_keys(contacto_nombre)
search_box.send_keys(Keys.ENTER)

time.sleep(2)  # Esperar un poco para asegurarse de que se cargue la conversación

# Encontrar el campo de texto para escribir el mensaje y enviarlo
mensaje_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
mensaje_box.click()
mensaje_box.send_keys(mensaje)
mensaje_box.send_keys(Keys.ENTER)

# Cerrar el navegador
# driver.quit()  # Si deseas cerrar el navegador al finalizar

print("Mensaje enviado con éxito.")
