class DispositivoElectronico:
    def __init__(self, memoria, ram, procesador):
        self.memoria = memoria
        self.ram = ram
        self.procesador = procesador
        self.apps_instaladas = []
        self.encendido = False

    def encender(self):
        if not self.encendido:
            print("Encendiendo dispositivo...")
            self.encendido = True
        else:
            print("El dispositivo ya está encendido.")

    def apagar(self):
        if self.encendido:
            print("Apagando dispositivo...")
            self.encendido = False
        else:
            print("El dispositivo ya está apagado.")

    def instalar_app(self, app_nombre):
        if self.encendido:
            if self.memoria >= 100:
                self.apps_instaladas.append(app_nombre)
                self.memoria -= 100
                print(f"App {app_nombre} instalada correctamente.")
            else:
                print("Memoria insuficiente para instalar la app.")
        else:
            print("Enciende el dispositivo antes de instalar una app.")

    def desinstalar_app(self, app_nombre):
        if self.encendido:
            if app_nombre in self.apps_instaladas:
                self.apps_instaladas.remove(app_nombre)
                self.memoria += 100
                print(f"App {app_nombre} desinstalada correctamente.")
            else:
                print("La app no está instalada.")
        else:
            print("Enciende el dispositivo antes de desinstalar una app.")


class TelefonoMovil(DispositivoElectronico):
    def __init__(self, memoria, ram, procesador, numero_telefono):
        super().__init__(memoria, ram, procesador)
        self.numero_telefono = numero_telefono

    def enviar_bizum(self, receptor, monto, cuenta_emisor, cuenta_receptor):
        if self.encendido:
            print(f"Enviando un Bizum de {monto}€ a {receptor}")
            if cuenta_emisor.saldo >= monto:
                cuenta_emisor.actualizar_saldo(-monto)
                cuenta_receptor.actualizar_saldo(monto)
                print("Bizum enviado correctamente.")
            else:
                print("Saldo insuficiente para realizar el envío de Bizum.")
        else:
            print("Enciende el dispositivo antes de enviar un Bizum.")


class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def actualizar_saldo(self, monto):
        self.saldo += monto


cuenta_emisor = CuentaBancaria("Nacho", 1000)
cuenta_receptor = CuentaBancaria("Jaime", 500)

telefono = TelefonoMovil(220, 4, "Apple A19", "123456789")

telefono.encender()
telefono.enviar_bizum("987654321", 20, cuenta_emisor, cuenta_receptor)
print("Saldo emisor:", cuenta_emisor.saldo)
print("Saldo receptor:", cuenta_receptor.saldo)
telefono.apagar()
