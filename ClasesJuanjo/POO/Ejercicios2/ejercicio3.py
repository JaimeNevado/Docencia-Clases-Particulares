class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad no puede ser negativa")
        else:
            self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad no puede ser negativa")
        else:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
            else:
                print("No se puede realizar la operación. Saldo insuficiente.")

    def obtener_saldo(self):
        return self.saldo

    def __str__(self):
        return f"Titular: {self.titular}, Saldo: {self.saldo}"

    def __eq__(self, otra_cuenta):
        return self.titular == otra_cuenta.titular


# Crear dos objetos de la clase CuentaBancaria
cuenta1 = CuentaBancaria("Juan Pérez", 1000)
cuenta2 = CuentaBancaria("María López", 2000)

# Realizar operaciones de depósito y retiro
cuenta1.depositar(500)
cuenta2.retirar(300)

# Realizar operaciones de comparación
if cuenta1 == cuenta2:
    print("Ambas cuentas tienen el mismo titular.")
else:
    print("Las cuentas tienen diferentes titulares.")

# Mostrar información actualizada de las cuentas
print("Información de la cuenta 1:", cuenta1)
print("Información de la cuenta 2:", cuenta2)
