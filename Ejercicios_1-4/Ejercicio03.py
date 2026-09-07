class CuentaBancaria:
    def __init__(self, titular="Angel", nroCuenta="123456", saldo=1000.0):
        self.__titular = titular
        self.__nroCuenta = nroCuenta
        self.__saldo = saldo

    # a) y c) 
    def depositar(self, monto):
        if monto <= 0:
            print("Error: No se puede depositar una cantidad menor o igual a 0.")
        else:
            self.__saldo += monto
            print(f"Deposito exitoso de Bs. {monto}. Saldo actual: Bs. {self.__saldo}")

    # a) y b) 
    def retirar(self, monto):
        if monto > self.__saldo:
            print(f"Error: Saldo insuficiente. Intenta retirar Bs. {monto}, pero el saldo es Bs. {self.__saldo}.")
        else:
            self.__saldo -= monto
            print(f"Retiro exitoso de Bs. {monto}. Saldo actual: Bs. {self.__saldo}")

    # d) 
    def mostrarDatos(self):
        print(f"Titular: {self.__titular} | Nro Cuenta: {self.__nroCuenta} | Saldo: Bs. {self.__saldo}")


class Main():
    cuenta = CuentaBancaria("Angel Torrez", "45678912", 500.0)

    print("--- DATOS INICIALES ---")
    cuenta.mostrarDatos()
    print()

    print("--- PRUEBAS DE DEPOSITO ---")
    # Caso correcto
    cuenta.depositar(200.0)
    # Caso error (negativo o 0)
    cuenta.depositar(-50.0)
    cuenta.depositar(0)
    print()

    print("--- PRUEBAS DE RETIRO ---")
    # Caso correcto
    cuenta.retirar(150.0)
    # Caso error (retirar mas de lo disponible)
    cuenta.retirar(800.0)
    print()

    print("--- DATOS FINALES ---")
    cuenta.mostrarDatos()