
class Biblioteca:
    __nombre: str
    __direccion: str
    __telefono:str
    __listaLibros: list
    
    def __init__(self,nombre,direccion,telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__listaLibros = []
    
    def AgregarLibro(self, unlibro):
        self.__listaLibros.append(unlibro)
    
    def getNombre(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion

    def getTelefono(self):
        return self.__telefono
    
    def ComplementoIncisoByC(self,titulo, condicion):
        encontrado = False
        indice = 0
        
        while indice < len(self.__listaLibros) and encontrado == False:
            if self.__listaLibros[indice].get_titulo() == titulo and condicion == "ELIMINAR":
                encontrado = True
                self.__listaLibros.pop(indice)
                print("Eliminado Existosamente")
            elif self.__listaLibros[indice].get_titulo() == titulo and condicion == "BUSCAR":
                encontrado = True
                print("El libro con titulo {} se encuentra en la biblioteca: {}".format(titulo,self.__nombre))
                print (self.__listaLibros[indice])
            else:
                indice += 1
        
        if encontrado == False:
            print("No se encontro el libro con ese titulo.")
    
    def ListarLibros(self):
        indice = 0
        
        print("La biblioteca {} posee los siguientes libros:".format(self.__nombre))
        for indice in range(len(self.__listaLibros)):
            print("\n{}".format(self.__listaLibros[indice].get_titulo()))
        
    
       
    def __str__(self):
        cadena1 = "\nNombre: {} || ".format(self.__nombre)
        cadena2 = "Direccion: {} || ".format(self.__direccion)
        cadena3 = "Telefono: {} || \n".format(self.__telefono)
        
        supercadena = cadena1+cadena2+cadena3
        return supercadena