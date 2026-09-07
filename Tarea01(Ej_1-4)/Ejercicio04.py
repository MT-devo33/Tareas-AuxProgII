class Bus:
    def __init__(self, capacidad=40, pasajeros=0, costo_pasaje=1.50):
        self.__capacidad = capacidad
        self.__pasajeros = pasajeros
        self.__costo_pasaje = costo_pasaje
        self.__dinero_recaudado = 0.0

    # a) 
    def subirPasajeros(self, x):
        asientos_libres = self.__capacidad - self.__pasajeros
        if x <= asientos_libres:
            self.__pasajeros += x
            print(f"Subieron {x} pasajeros con exito. Pasajeros a bordo: {self.__pasajeros}")
        else:
            print(f"No hay suficiente espacio para {x} pasajeros. Asientos disponibles: {asientos_libres}")

    # b) 
    def cobrarPasaje(self):
        total_cobro = self.__pasajeros * self.__costo_pasaje
        self.__dinero_recaudado += total_cobro
        print(f"Se cobro a {self.__pasajeros} pasajeros. Total recaudado en este cobro: Bs. {total_cobro:.2f}")

    # c) 
    def mostrarAsientosDisponibles(self):
        disponibles = self.__capacidad - self.__pasajeros
        print(f"Asientos disponibles: {disponibles} de {self.__capacidad}")

    def mostrarDatos(self):
        print(f"Capacidad: {self.__capacidad} | Pasajeros: {self.__pasajeros} | Recaudado: Bs. {self.__dinero_recaudado:.2f}")


class Main():
    # d) 
    b = Bus(capacidad=30, pasajeros=10, costo_pasaje=1.50)

    print("--- DATOS INICIALES ---")
    b.mostrarDatos()
    b.mostrarAsientosDisponibles()
    print()

    # a) 
    print("--- SUBIENDO PASAJEROS ---")
    b.subirPasajeros(15)
    b.subirPasajeros(10)
    print()

    # c) 
    print("--- ASIENTOS DISPONIBLES ---")
    b.mostrarAsientosDisponibles()
    print()

    # b) 
    print("--- COBRO DE PASAJES ---")
    b.cobrarPasaje()
    print()

    print("--- ESTADO FINAL DEL BUS ---")
    b.mostrarDatos()