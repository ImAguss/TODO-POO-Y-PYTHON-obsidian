
class Libro:
    __titulo:str
    __autor:str
    __lsbn:str
    __genero:str
    
    def __init__(self,titulo,autor,lsbn,genero):
        self.__titulo = titulo
        self.__autor = autor
        self.__lsbn = lsbn
        self.__genero = genero
    
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_lsbn(self):
        return self.__lsbn

    def get_genero(self):
        return self.__genero
    
    def __str__(self):
        cadena1 = "Autor: || {}".format(self.__autor)
        cadena2 = "Genero: || {}".format(self.__genero)
        
        supercadena =  cadena1 + cadena2
        
        return supercadena