class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito de {cantidad} realizado. Saldo actual: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Saldo actual: {self.saldo}")
        else:
            print("No hay saldo suficiente para realizar el retiro.")

    def obtener_saldo(self):
        return self.saldo

    def __eq__(self, otra_cuenta):
        return self.titular == otra_cuenta.titular

# Crear dos cuentas bancarias
cuenta1 = CuentaBancaria("Juan", 1000)
cuenta2 = CuentaBancaria("Maria", 500)

# Realizar operaciones de depósito y retiro
cuenta1.depositar(200)
cuenta2.retirar(100)

# Mostrar información de las cuentas
print(f"Saldo de la cuenta de {cuenta1.titular}: {cuenta1.obtener_saldo()}")
print(f"Saldo de la cuenta de {cuenta2.titular}: {cuenta2.obtener_saldo()}")

# Mostrar si los titulares son iguales o no
if cuenta1 == cuenta2:
    print("Los titulares de las cuentas son iguales.")
else:
    print("Los titulares de las cuentas son diferentes.")
