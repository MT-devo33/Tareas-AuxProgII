class Documento:
    def __init__(self, titulo, autor, editorial, anio):
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__anio = anio

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_editorial(self):
        return self.__editorial

    def get_anio(self):
        return self.__anio

    def es_libro(self):
        return False

    def es_revista(self):
        return False

    def copiar(self):
        pass


class Libro(Documento):
    def __init__(self, titulo, autor, editorial, anio):
        super().__init__(titulo, autor, editorial, anio)

    def es_libro(self):
        return True

    def copiar(self):
        return Libro(self.get_titulo(), self.get_autor(), self.get_editorial(), self.get_anio())


class Revista(Documento):
    def __init__(self, titulo, autor, editorial, anio, volumen, numero, mes):
        super().__init__(titulo, autor, editorial, anio)
        self.__volumen = volumen
        self.__numero = numero
        self.__mes = mes

    def get_volumen(self):
        return self.__volumen

    def get_numero(self):
        return self.__numero

    def get_mes(self):
        return self.__mes

    def es_revista(self):
        return True

    def copiar(self):
        return Revista(self.get_titulo(), self.get_autor(), self.get_editorial(), self.get_anio(), self.__volumen, self.__numero, self.__mes)


class DocumentoCD(Documento):
    def __init__(self, titulo, autor, editorial, anio, formato, licencia):
        super().__init__(titulo, autor, editorial, anio)
        self.__formato = formato
        self.__licencia = licencia

    def get_formato(self):
        return self.__formato

    def get_licencia(self):
        return self.__licencia

    def copiar(self):
        return DocumentoCD(self.get_titulo(), self.get_autor(), self.get_editorial(), self.get_anio(), self.__formato, self.__licencia)


class RevistaInvestigacion(Revista):
    def __init__(self, titulo, autor, editorial, anio, volumen, numero, mes, campo_investigacion):
        super().__init__(titulo, autor, editorial, anio, volumen, numero, mes)
        self.__campo_investigacion = campo_investigacion

    def get_campo_investigacion(self):
        return self.__campo_investigacion

    def copiar(self):
        return RevistaInvestigacion(self.get_titulo(), self.get_autor(), self.get_editorial(), self.get_anio(), self.get_volumen(), self.get_numero(), self.get_mes(), self.__campo_investigacion)


class Biblioteca:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__documentos = []

    def get_nombre(self):
        return self.__nombre

    def agregar_documento(self, doc):
        self.__documentos.append(doc)

    def obtener_documentos(self):
        return self.__documentos

    def limpiar_documentos(self):
        self.__documentos = []

    def contar_revistas(self):
        contador = 0
        for doc in self.__documentos:
            if doc.es_revista():
                contador += 1
        return contador

    def contar_documentos(self):
        contador = 0
        for doc in self.__documentos:
            contador += 1
        return contador

    def mostrar_comparacion(self, otra_biblioteca):
        docs_propios = self.contar_documentos()
        docs_otros = otra_biblioteca.contar_documentos()
        revs_propias = self.contar_revistas()
        revs_otras = otra_biblioteca.contar_revistas()

        if docs_propios > docs_otros:
            print(f"La biblioteca {self.__nombre} tiene más documentos ({docs_propios} frente a {docs_otros}).")
        elif docs_otros > docs_propios:
            print(f"La biblioteca {otra_biblioteca.get_nombre()} tiene más documentos ({docs_otros} frente a {docs_propios}).")
        else:
            print(f"Ambas bibliotecas tienen la misma cantidad de documentos ({docs_propios}).")

        if revs_propias > revs_otras:
            print(f"La biblioteca {self.__nombre} tiene más revistas ({revs_propias} frente a {revs_otras}).")
        elif revs_otras > revs_propias:
            print(f"La biblioteca {otra_biblioteca.get_nombre()} tiene más revistas ({revs_otras} frente a {revs_propias}).")
        else:
            print(f"Ambas bibliotecas tienen la misma cantidad de revistas ({revs_propias}).")

    def copiar_seguridad(self, sufijo):
        copia_bib = Biblioteca(self.__nombre + sufijo)
        for doc in self.__documentos:
            copia_bib.agregar_documento(doc.copiar())
        return copia_bib


class Main():
    bib1 = Biblioteca("Central")
    bib2 = Biblioteca("Ciencias")

    l1 = Libro("Estructuras de Datos", "Joyanes", "McGraw Hill", 2008)
    l2 = Libro("Ingeniería de Software", "Sommerville", "Pearson", 2011)
    r1 = Revista("PC World", "Varios", "IDG", 2026, 12, 4, "Abril")
    r2 = Revista("National Geographic", "Varios", "NatGeo", 2026, 150, 10, "Octubre")
    cd1 = DocumentoCD("Ubuntu Server", "Canonical", "GPL", 2024, "ISO", "Open Source")
    ri1 = RevistaInvestigacion("IEEE Transactions", "IEEE", "IEEE Press", 2025, 5, 2, "Febrero", "Inteligencia Artificial")

    bib1.agregar_documento(l1)
    bib1.agregar_documento(r1)
    bib1.agregar_documento(cd1)

    bib2.agregar_documento(l2)
    bib2.agregar_documento(r2)
    bib2.agregar_documento(ri1)

    print(f"--- ESTADO INICIAL ---")
    bib1.mostrar_comparacion(bib2)

    print(f"\n--- TRASLADO DE DOCUMENTOS ---")
    documentos_totales = []
    
    for doc in bib1.obtener_documentos():
        documentos_totales.append(doc)
    for doc in bib2.obtener_documentos():
        documentos_totales.append(doc)
        
    bib1.limpiar_documentos()
    bib2.limpiar_documentos()

    for doc in documentos_totales:
        if doc.es_revista():
            bib1.agregar_documento(doc)
        elif doc.es_libro():
            bib2.agregar_documento(doc)
        else:
            bib1.agregar_documento(doc)

    print(f"Traslado completado. Todas las revistas están en {bib1.get_nombre()} y los libros en {bib2.get_nombre()}.")
    bib1.mostrar_comparacion(bib2)

    print(f"\n--- COPIA DE SEGURIDAD ---")
    backup_bib1 = bib1.copiar_seguridad("_Backup")
    backup_bib2 = bib2.copiar_seguridad("_Backup")
    
    print(f"Copia generada: {backup_bib1.get_nombre()} con {backup_bib1.contar_documentos()} documentos guardados dato a dato.")
    print(f"Copia generada: {backup_bib2.get_nombre()} con {backup_bib2.contar_documentos()} documentos guardados dato a dato.")