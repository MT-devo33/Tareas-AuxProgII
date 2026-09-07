class Vehiculo:
    def __init__(self, marca="Toyota", modelo="Corolla", anio=2020, kilometraje=50, color="Blanco"):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__kilometraje = kilometraje
        self.__color = color

    # a)
    def mostrarKilometraje(self):
        metros = self.__kilometraje * 1000
        print(f"Kilometraje: {self.__kilometraje} km ({metros} metros)")

    # b)
    def cambiarColor(self, nuevo_color):
        self.__color = nuevo_color

    def mostrarDatos(self):
        print(f"Vehiculo: {self.__marca} {self.__modelo}, Anio: {self.__anio}, Color: {self.__color}")


class Main():
    # c) 
    auto1 = Vehiculo("Toyota", "Corolla", 2020, 50, "Blanco")
    auto2 = Vehiculo("Nissan", "Sentra", 2018, 120, "Gris")

    print("--- AUTO 1 ---")
    auto1.cambiarColor("Rojo")
    auto1.mostrarDatos()
    auto1.mostrarKilometraje()

    print()

    print("--- AUTO 2 ---")
    auto2.cambiarColor("Negro")
    auto2.mostrarDatos()
    auto2.mostrarKilometraje()