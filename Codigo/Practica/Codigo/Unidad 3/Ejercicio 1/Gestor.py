import csv
from ClaseHotel import Hotel

class Gestor:
    __Hoteles: list

    def __init__(self):
        self.__Hoteles = []

    def CargaCsv(self):
        with open("Hoteles.csv") as archivo:
            reader = csv.reader(archivo, delimiter=';')
            Hotel_Actual = None
            for fila in reader:
                try:
                    if "Hotel" in fila[0]:
                        Hotel_Actual = Hotel(fila[0], fila[1], fila[2])
                        self.__Hoteles.append(Hotel_Actual)
                    else:
                        if Hotel_Actual is not None:
                            Hotel_Actual.AgregarHabitacion(fila[0], fila[1], fila[2], fila[3],fila[4])
                except IndexError:
                    print(f"Fila incompleta o mal formada: {fila}")
                except Exception as e:
                    print(f"Error inesperado al cargar: {e}")

    def BusquedaHotelPorNombre(self, nombreHotel):
        indice = 0
        while indice < len(self.__Hoteles):
            try:
                if self.__Hoteles[indice].getNombre().lower() == nombreHotel.lower():
                    return indice
            except AttributeError:
                print(f"Error: El objeto en la posición {indice} no es un hotel válido.")
            indice += 1
        return None

    def AgregarHabitacion(self, nombreHotel):
        try:
            indice = self.BusquedaHotelPorNombre(nombreHotel)
            if indice is None:
                raise ValueError("No se encontró el Hotel.")
            print("Agregando Habitacion para hotel: {}".format(nombreHotel.upper()))
            numero = str(input("Ingrese Numero de Habitacion: "))
            piso = str(input("Ingrese el piso: "))
            tipo = str(input("Ingrese el tipo: "))
            precio = str(input("Ingrese el Precio:"))
            self.__Hoteles[indice].AgregarHabitacion(numero, piso, tipo, precio)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"Error inesperado: {e}")

    def ReservarHabitacion(self, numero, nombreHotel):
        try:
            indice = self.BusquedaHotelPorNombre(nombreHotel)
            if indice is None:
                raise ValueError("No se encontró el Hotel.")
            encontrado = self.__Hoteles[indice].Reservar_O_LiberarHabitacion(numero, "Reservar")
            if encontrado:
                print("Se reservó exitosamente")
            else:
                raise LookupError(f"No se encontró la habitación con el número: {numero}")
        except (ValueError, LookupError) as e:
            print(e)
        except Exception as e:
            print(f"Error inesperado: {e}")

    def LiberarHabitacion(self, numero, nombreHotel):
        try:
            indice = self.BusquedaHotelPorNombre(nombreHotel)
            if indice is None:
                raise ValueError("No se encontró el Hotel.")
            encontrado = self.__Hoteles[indice].Reservar_O_LiberarHabitacion(numero, "Liberar")
            if encontrado:
                print("Se liberó exitosamente")
            else:
                raise LookupError(f"No se encontró la habitación con el número: {numero}")
        except (ValueError, LookupError) as e:
            print(e)
        except Exception as e:
            print(f"Error inesperado: {e}")

    def Inciso4(self, nombreHotel, tipo):
        try:
            indice = self.BusquedaHotelPorNombre(nombreHotel)
            if indice is None:
                raise ValueError("No se encontró el Hotel.")
            self.__Hoteles[indice].Inciso4(tipo)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"Error inesperado: {e}")

    def HabitacionLibrePorPiso(self, nombreHotel):
        try:
            indice = self.BusquedaHotelPorNombre(nombreHotel)
            if indice is None:
                raise ValueError("No se encontró el Hotel.")
            self.__Hoteles[indice].HabitacionesLibresPorPiso()
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"Error inesperado: {e}")

    def MostrarDetallesPorTipo(self, nombreHotel):
        try:
            indice = self.BusquedaHotelPorNombre(nombreHotel)
            if indice is None:
                raise ValueError("No se encontró el Hotel.")
            self.__Hoteles[indice].OrdenarHabitacionesPorTipo()
            self.__Hoteles[indice].ImprimirTabla()
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"Error inesperado: {e}")

    def listarHoteles(self):
        for hotel in self.__Hoteles:
            print("-", hotel.getNombre())