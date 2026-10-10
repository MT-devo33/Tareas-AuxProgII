import math
from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    @abstractmethod
    def obtenerArea(self):
        pass


class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self.__lado = lado

    def obtenerArea(self):
        return self.__lado * self.__lado


class Triangulo(Figura):
    def __init__(self, color, lado1, lado2, lado3):
        super().__init__(color)
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    def obtenerArea(self):
        s = (self.__lado1 + self.__lado2 + self.__lado3) / 2
        return math.sqrt(s * (s - self.__lado1) * (s - self.__lado2) * (s - self.__lado3))


class Redondo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.__radio = radio

    def obtenerArea(self):
        return math.pi * self.__radio * self.__radio


class Main:
    cuadrado1 = Cuadrado("Rojo", 4)
    cuadrado2 = Cuadrado("Azul", 5)
    
    triangulo1 = Triangulo("Verde", 3, 4, 5)
    triangulo2 = Triangulo("Amarillo", 6, 8, 10)
    
    redondo1 = Redondo("Naranja", 3)
    redondo2 = Redondo("Morado", 7)
    
    print(f"Cuadrado 1 - Color: {cuadrado1.get_color()}, Área: {cuadrado1.obtenerArea()}")
    print(f"Cuadrado 2 - Color: {cuadrado2.get_color()}, Área: {cuadrado2.obtenerArea()}")
    print(f"Triángulo 1 - Color: {triangulo1.get_color()}, Área: {triangulo1.obtenerArea()}")
    print(f"Triángulo 2 - Color: {triangulo2.get_color()}, Área: {triangulo2.obtenerArea()}")
    print(f"Redondo 1 - Color: {redondo1.get_color()}, Área: {redondo1.obtenerArea():.2f}")
    print(f"Redondo 2 - Color: {redondo2.get_color()}, Área: {redondo2.obtenerArea():.2f}")
    
    print("\n--- COMPARACIÓN DE ÁREAS ---")
    area_cuad = cuadrado1.obtenerArea()
    area_tri = triangulo1.obtenerArea()
    
    if area_cuad > area_tri:
        print(f"La figura con mayor área es de color: {cuadrado1.get_color()}")
    elif area_tri > area_cuad:
        print(f"La figura con mayor área es de color: {triangulo1.get_color()}")
    else:
        print("Ambas figuras tienen la misma área")