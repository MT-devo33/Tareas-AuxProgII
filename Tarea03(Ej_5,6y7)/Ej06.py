class Animal:
    def __init__(self, edad, peso, especie):
        self.__edad = edad
        self.__peso = peso
        self.__especie = especie

    def get_edad(self):
        return self.__edad

    def get_peso(self):
        return self.__peso

    def get_especie(self):
        return self.__especie

    def respirar(self):
        return "Toma oxígeno."

    def mover(self):
        return "Se desplaza de un lugar a otro."


class Terrestre(Animal):
    def __init__(self, edad, peso, especie, num_patas, tipo_terreno):
        super().__init__(edad, peso, especie)
        self.__num_patas = num_patas
        self.__tipo_terreno = tipo_terreno

    def get_num_patas(self):
        return self.__num_patas

    def get_tipo_terreno(self):
        return self.__tipo_terreno

    def caminar(self):
        return f"El {self.get_especie()} está caminando."

    def correr(self):
        return f"El {self.get_especie()} está corriendo rápido."

    def respirar(self):
        return f"{super().respirar()} Respira oxígeno del aire mediante pulmones."

    def mover(self):
        return f"{super().mover()} Especialización: Se mueve caminando o corriendo sobre la tierra."


class Acuatico(Animal):
    def __init__(self, edad, peso, especie, tipo_agua, num_aletas):
        super().__init__(edad, peso, especie)
        self.__tipo_agua = tipo_agua
        self.__num_aletas = num_aletas

    def get_tipo_agua(self):
        return self.__tipo_agua

    def get_num_aletas(self):
        return self.__num_aletas

    def nadar(self):
        return f"El {self.get_especie()} está nadando."

    def sumergir(self):
        return f"El {self.get_especie()} se ha sumergido."

    def respirar(self):
        return f"{super().respirar()} Respira oxígeno disuelto en el agua mediante branquias."

    def mover(self):
        return f"{super().mover()} Especialización: Se mueve nadando bajo el agua."


class Aereo(Animal):
    def __init__(self, edad, peso, especie, envergadura, altitud_maxima):
        super().__init__(edad, peso, especie)
        self.__envergadura = envergadura
        self.__altitud_maxima = altitud_maxima

    def get_envergadura(self):
        return self.__envergadura

    def get_altitud_maxima(self):
        return self.__altitud_maxima

    def volar(self):
        return f"El {self.get_especie()} está volando."

    def aterrizar(self):
        return f"El {self.get_especie()} ha aterrizado."

    def respirar(self):
        return f"{super().respirar()} Respira oxígeno del aire durante el vuelo."

    def mover(self):
        return f"{super().mover()} Especialización: Se mueve volando por los aires."


class Main:
    leon = Terrestre(5, 190.5, "León", 4, "Sabana")
    tiburon = Acuatico(8, 450.0, "Tiburón Blanco", "Salada", 5)
    aguila = Aereo(3, 6.2, "Águila Real", 2.3, 3000.0)

    print(f"--- DATOS ANIMAL TERRESTRE ---")
    print(f"Especie: {leon.get_especie()}, Edad: {leon.get_edad()} años, Peso: {leon.get_peso()} kg")
    print(f"Patas: {leon.get_num_patas()}, Terreno: {leon.get_tipo_terreno()}")
    print(f"Respirar: {leon.respirar()}")
    print(f"Mover: {leon.mover()}")
    print(f"Acciones propias: {leon.caminar()} | {leon.correr()}")

    print(f"\n--- DATOS ANIMAL ACUÁTICO ---")
    print(f"Especie: {tiburon.get_especie()}, Edad: {tiburon.get_edad()} años, Peso: {tiburon.get_peso()} kg")
    print(f"Agua: {tiburon.get_tipo_agua()}, Aletas: {tiburon.get_num_aletas()}")
    print(f"Respirar: {tiburon.respirar()}")
    print(f"Mover: {tiburon.mover()}")
    print(f"Acciones propias: {tiburon.nadar()} | {tiburon.sumergir()}")

    print(f"\n--- DATOS ANIMAL AÉREO ---")
    print(f"Especie: {aguila.get_especie()}, Edad: {aguila.get_edad()} años, Peso: {aguila.get_peso()} kg")
    print(f"Envergadura: {aguila.get_envergadura()} m, Altitud Máx: {aguila.get_altitud_maxima()} m")
    print(f"Respirar: {aguila.respirar()}")
    print(f"Mover: {aguila.mover()}")
    print(f"Acciones propias: {aguila.volar()} | {aguila.aterrizar()}")