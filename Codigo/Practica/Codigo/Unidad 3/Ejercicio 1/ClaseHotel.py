from ClaseHabitacion import Habitacion

class Hotel:
    __nombre: str
    __direccion: str
    __telefono: str
    __listaHabitaciones: list
    
    def __init__(self,nombre,direccion,telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__listaHabitaciones = []
    
    def getNombre(self):
        return self.__nombre
        
    def AgregarHabitacion(self,numero, piso, tipo, precio,disponibilidad):
        # Evita habitaciones duplicadas
        for hab in self.__listaHabitaciones:
            if hab.getNumero() == numero:
                raise ValueError(f"Ya existe una habitación con el número {numero}.")
        habitacion = Habitacion(numero,piso,tipo,precio,disponibilidad)
        self.__listaHabitaciones.append(habitacion)
        
    def getlistaHabitaciones(self):
        return self.__listaHabitaciones
    
    def Reservar_O_LiberarHabitacion(self, numero, condicion):
        encontrado = False
        indice = 0
        if condicion == "Reservar":
            while indice < len(self.__listaHabitaciones) and encontrado == False:
                if self.__listaHabitaciones[indice].getNumero() == numero:
                    encontrado = True
                    self.__listaHabitaciones[indice].setDisponibilidad(True)
                else:
                    indice +=1
        elif condicion == "Liberar":
            while indice < len(self.__listaHabitaciones) and encontrado == False:
                if self.__listaHabitaciones[indice].getNumero() == numero:
                    encontrado = True
                    self.__listaHabitaciones[indice].setDisponibilidad(True)
                else:
                    indice +=1
        if not encontrado:
            raise ValueError(f"No existe la habitación con el número {numero}.")
        return encontrado
                                   
    def Inciso4 (self, tipo):
        indice = 0
        encontrado = False
        for indice in range (len(self.__listaHabitaciones)):
            if self.__listaHabitaciones[indice].getTipo() == tipo:
                print ("\nNumero: {}".format(self.__listaHabitaciones[indice].getNumero()))
                print ("Piso: {}\n".format(self.__listaHabitaciones[indice].getPiso()))
                encontrado = True
        if not encontrado:
            raise ValueError(f"No hay habitaciones del tipo '{tipo}'.")
    
    def OrdenarHabitacionesPorTipo(self):
        n = len(self.__listaHabitaciones)
        for i in range (n-1):
            for j in range (n-i-1):
                if self.__listaHabitaciones[j+1].getTipo() < self.__listaHabitaciones[j].getTipo():
                    temp = self.__listaHabitaciones[j]
                    self.__listaHabitaciones[j] = self.__listaHabitaciones[j+1]
                    self.__listaHabitaciones[j+1] = temp
    
    def HabitacionesLibresPorPiso(self):
        piso = 0
        for piso in range (4):
            print ("Piso : {}".format(piso+1))
            indice = 0
            hay_libres = False
            for indice in range(len(self.__listaHabitaciones)):
                if(self.__listaHabitaciones[indice].getPiso() == piso+1) and (self.__listaHabitaciones[indice].getDisponibilidad() == "False"):
                    print ("Habitacion Numero: {}".format(self.__listaHabitaciones[indice].getNumero()))
                    print("Esta Libre\n")
                    hay_libres = True
            if not hay_libres:
                print("No hay habitaciones libres en este piso.")
                    
    def ImprimirTabla(self):
        indice = 0
        if not self.__listaHabitaciones:
            raise ValueError("No hay habitaciones para mostrar.")
        for indice in range(len(self.__listaHabitaciones)):
            print(self.__listaHabitaciones[indice])


