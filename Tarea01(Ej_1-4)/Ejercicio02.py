class Computadora:
    def __init__(self, marca="HP", procesador="Core i5", ram=8, almacenamiento=512):
        self.__marca = marca
        self.__procesador = procesador
        self.__ram = ram
        self.__almacenamiento = almacenamiento

    def getMarca(self):
        return self.__marca

    def getProcesador(self):
        return self.__procesador

    def getRam(self):
        return self.__ram

    def getAlmacenamiento(self):
        return self.__almacenamiento

    # b) 
    def verificarRam(self, x):
        if self.__ram == x:
            print(f"La computadora {self.__marca} tiene {x} GB de RAM (Es igual a X)")
        else:
            print(f"La computadora {self.__marca} NO tiene {x} GB de RAM (Tiene {self.__ram} GB)")

    def mostrarDatos(self):
        print(f"Marca: {self.__marca}, Procesador: {self.__procesador}, RAM: {self.__ram}GB, Almacenamiento: {self.__almacenamiento}GB")


class Main():
    # a) 
    # Forma 1: Usando los valores por defecto del constructor
    c1 = Computadora()

    # Forma 2: Pasando los valores explicitos por parametro
    c2 = Computadora("Dell", "Ryzen 7", 16, 1024)

    print("--- COMPUTADORA 1 ---")
    c1.mostrarDatos()

    print()

    print("--- COMPUTADORA 2 ---")
    c2.mostrarDatos()

    print()

    # b) 
    x = 8
    print(f"--- VERIFICACION DE RAM CON X = {x} ---")
    c1.verificarRam(x)
    c2.verificarRam(x)

    print()

    # c) 
    print("--- COMPUTADORA CON MAYOR ALMACENAMIENTO ---")
    if c1.getAlmacenamiento() > c2.getAlmacenamiento():
        c1.mostrarDatos()
    else:
        c2.mostrarDatos()