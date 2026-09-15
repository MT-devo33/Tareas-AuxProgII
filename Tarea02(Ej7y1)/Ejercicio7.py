class Auto:
    # a)
    def __init__(self, marca="Toyota", color="Blanco", gasolina=20):
        self.__marca = marca
        self.__color = color
        self.__gasolina = gasolina

    def getMarca(self):
        return self.__marca

    def getColor(self):
        return self.__color

    def getGasolina(self):
        return self.__gasolina

    # c)
    def __pos__(self):
        self.__gasolina += 5
        return self

    # d)
    def __add__(self, nuevo_color):
        self.__color = nuevo_color
        return self

    # e)
    def __sub__(self, otro):
        total_gasolina = self.__gasolina + otro.getGasolina()
        return total_gasolina

    def mostrarDatos(self):
        print(f"Auto: {self.__marca} | Color: {self.__color} | Gasolina: {self.__gasolina} litros")


class Main():
    # b)
    auto1 = Auto()

    auto2 = Auto("Nissan", "Azul", 35)

    print("--- ESTADO INICIAL ---")
    auto1.mostrarDatos()
    auto2.mostrarDatos()
    print()

    # c)
    +auto1
    print("--- DESPUES DE INCREMENTAR GASOLINA A AUTO 1 (+5L) ---")
    auto1.mostrarDatos()
    print()

    # d)
    auto1 + "Rojo"
    auto2 + "Negro"
    print("--- DESPUES DE CAMBIAR DE COLOR CON OPERADOR + ---")
    auto1.mostrarDatos()
    auto2.mostrarDatos()
    print()

    # e) 
    total = auto1 - auto2
    print("--- TOTAL DE GASOLINA (AUTO 1 - AUTO 2) ---")
    print(f"Total de gasolina acumulada: {total} litros")