class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = []
        self.status = 0

    def power_on(self):
        if self.status == 0:
            self.status = 1
            print("El teléfono se ha encendido.")
        else:
            print("El teléfono ya está encendido.")

    def power_off(self):
        if self.status == 1:
            self.status = 0
            print("El teléfono se ha apagado.")
        else:
            print("El teléfono ya está apagado.")

    def install_app(self, app):
        if self.status == 1:
            if app not in self.apps:
                self.apps.append(app)
                print(f"La aplicación {app} se ha instalado.")
            else:
                print(f"La aplicación {app} ya está instalada.")
        else:
            print("El teléfono está apagado. Debes encenderlo para instalar aplicaciones.")

    def uninstall_app(self, app):
        if self.status == 1:
            if app in self.apps:
                self.apps.remove(app)
                print(f"La aplicación {app} se ha desinstalado.")
            else:
                print(f"La aplicación {app} no está instalada.")
        else:
            print("El teléfono está apagado. Debes encenderlo para desinstalar aplicaciones.")

# Crear un iPhone
iPhone = MobilePhone("Apple", "6.5 pulgadas", 6)

# Encender el móvil
iPhone.power_on()

# Instalar aplicaciones
iPhone.install_app("Clash Royale")
iPhone.install_app("Minecraft")
iPhone.install_app("Youtube")

# Imprimir la lista de aplicaciones del móvil
print("Aplicaciones instaladas en el móvil:")
for app in iPhone.apps:
    print(app)
