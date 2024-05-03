class MobilePhone:
    def __init__(self):
        self.apps = []
        self.encendido = False

    def power_on(self):
        if self.encendido == False:
            self.encendido = True
            print("El teléfono se ha encendido.")
        else:
            print("El teléfono ya está encendido.")

    def power_off(self):
        if self.encendido == True:
            self.encendido = False
            print("El teléfono se ha apagado.")
        else:
            print("El teléfono ya está apagado.")

    def install_app(self, app):
        if self.encendido == True:
            if app not in self.apps:
                self.apps.append(app)
                print(f"La aplicación '{app}' se ha instalado.")
            else:
                print(f"La aplicación '{app}' ya está instalada.")
        else:
            print("El teléfono está apagado. Enciéndelo para instalar aplicaciones.")

    def uninstall_app(self, app):
        if self.encendido == True:
            if app in self.apps:
                self.apps.remove(app)
                print(f"La aplicación '{app}' se ha desinstalado.")
            else:
                print(f"La aplicación '{app}' no está instalada.")
        else:
            print("El teléfono está apagado. Enciéndelo para desinstalar aplicaciones.")

# Crear un iPhone
iphone = MobilePhone()

# Encender el móvil
iphone.power_on()

# Instalar aplicaciones
iphone.install_app("Clash Royale")
iphone.install_app("Minecraft")
iphone.install_app("Youtube")

# Imprimir lista de apps
print("Aplicaciones instaladas en el móvil:")
for app in iphone.apps:
    print(app)
