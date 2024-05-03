class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se depositaron {cantidad} unidades. Saldo actual: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("No se puede retirar más dinero del saldo disponible.")
        else:
            self.saldo -= cantidad
            print(f"Se retiraron {cantidad} unidades. Saldo actual: {self.saldo}")

    def obtener_saldo(self):
        return self.saldo

    def __eq__(self, otra_cuenta):
        if (self.titular == otra_cuenta.titular):
            return True
        else:
            return False

# Crear dos cuentas bancarias
cuenta1 = CuentaBancaria("Juan", 1000)
cuenta2 = CuentaBancaria("María", 500)

# Realizar operaciones en cuenta1
cuenta1.depositar(500)
cuenta1.retirar(200)

# Realizar operaciones en cuenta2
cuenta2.depositar(100)
cuenta2.retirar(700)

# Comparar las cuentas por titular
if cuenta1 == cuenta2:
    print("Las cuentas tienen el mismo titular.")
else:
    print("Las cuentas tienen titulares diferentes.")

# Mostrar información de las cuentas
print("Información de la cuenta 1:")
print(f"Titular: {cuenta1.titular}, Saldo: {cuenta1.obtener_saldo()}")

print("Información de la cuenta 2:")
print(f"Titular: {cuenta2.titular}, Saldo: {cuenta2.obtener_saldo()}")
