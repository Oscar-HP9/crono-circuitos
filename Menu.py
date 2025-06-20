from Excepcion import CircuitosNombresIguales
from Circuito import Circuito
from Vehiculo import Coche, Moto
from Tiempo import Tiempo
from Crono import Crono
import json

class Menu:
    def __init__(self):
        self._opciones = {
            "1": ["VER LISTA DE CIRCUITOS.", self.ver_circuitos],
            "2": ["SELECCIONAR CIRCUITO POR ID.", self.seleccionar_circuito],
            "3": ["AÑADIR CIRCUITO.", self.añadir_circuito],
            "4": ["BORRAR CIRCUITO.", self.borrar_circuito],
            "5": ["TERMINAR PROGRAMA", self.salir_menu]
        }

        self._opciones_circuito = {
            "1": ["VER DETALLES DEL CIRCUITO Y CRONOS", self.detalles_circuito],
            "2": ["AGREGAR NUEVO CRONO", self.agregar_crono],
            "3": ["ELIMINAR CRONO", self.eliminar_crono],
            "4": ["REGRESAR AL MENU PRINCIPAL", self.salir_menu_circuito]
        }

        self.tipos_traccion = ["FWD","RWD","AWD","4WD"]

        self.circuitos = {}   #Diccionario de objetos Circuito con clave igual a su id y valor el objeto mismo

        self.circuito_actual = None

        self.quiere_salir_circuito = False

        self.quiere_salir = False

    #Funciones que manejan la logica de pedir y mostrar informacion y ejecutar metodos del menu
    def mostrar_opciones(self, opciones):
        cadena_opciones = "OPCIONES:\n"
        for id, opcion in opciones.items():
            cadena_opciones += f"{id}.____{opcion[0]}\n"
        print(cadena_opciones)

    def ingresar_opcion(self, opciones):
        while True:
            opcion = input("Ingresa el numero de la opcion que quieres elegir: ")
            if opcion in opciones:
                return opcion
            else:
                print("\n\tERROR! Ingrese una opcion valida.\n")

    def manejar_opcion(self, opcion, opciones):
        print("\n", f"{opciones[opcion][0]}".center(70, "-"))
        opciones[opcion][1]()
    #FIN Funciones que manejan la logica de pedir y mostrar informacion y ejecutar metodos del menu

    def crear_vehiculo(self):
        while True:
            tipo = input("De que tipo es su vehiculo (moto / coche)? ").lower()
            if tipo != "coche" and tipo != "moto":
                print("Tipo de vehiculo no reconocido, ingrese moto o coche como tipo")
            else:
                break
        while True:
            nombre_vehiculo_nuevo = input("Ingrese el nombre del vehiculo: ").strip()
            if not nombre_vehiculo_nuevo:
                print("El nombre no puede estar vacío.")
                continue
            break
        neumaticos = input("Ingrese los neumaticos del vehiculo, si lo desconoce solo imprima enter: ")
        if neumaticos == "":
            neumaticos = "No proporcionado"
        if tipo == "coche":
            while True:
                traccion = input( f"Ingrese el tipo de tracción del vehículo. Opciones: {self.tipos_traccion}. Para omitir, presione Enter: ").upper()
                if traccion == "":
                    traccion = "No especificado"
                    break
                elif traccion in self.tipos_traccion:
                    break
                elif traccion not in self.tipos_traccion:
                    print(f"Tipo de tracción desconocido. Opciones disponibles: {self.tipos_traccion}")
                    continue
            return Coche(nombre_vehiculo_nuevo, traccion, neumaticos)
        else:
            return Moto(nombre_vehiculo_nuevo, neumaticos)
    
    def crear_tiempo(self):
        while True:
            try:
                minutos = int(input("Ingrese los minutos: "))
                if minutos < 0:
                    print("Los minutos no pueden ser negativos.")
                    continue
                break
            except ValueError:
                print("ERROR: Ingrese un número entero válido para minutos.")

        while True:
            try:
                segundos = int(input("Ingrese los segundos (0-59): "))
                if not 0 <= segundos < 60:
                    print("Los segundos deben estar entre 0 y 59.")
                    continue
                break
            except ValueError:
                print("ERROR: Ingrese un número entero válido para segundos.")

        while True:
            try:
                fracciones = float(input("Ingrese las fracciones de segundo (ej. 0.356): "))
                if not 0 <= fracciones < 1:
                    print("Las fracciones deben ser un número positivo menor que 1.")
                    continue
                break
            except ValueError:
                print("ERROR: Ingrese un número decimal válido para fracciones de segundo.")

        return Tiempo(minutos, segundos, fracciones)

    #Funciones del menu ciruito
    def detalles_circuito(self):
        print(self.circuito_actual)
    
    def agregar_crono(self):
        vehiculo = self.crear_vehiculo()
        tiempo = self.crear_tiempo()
        nuevo_crono = Crono(vehiculo, tiempo)
        self.circuito_actual.cronos[nuevo_crono.id_crono] = nuevo_crono

    def eliminar_crono(self):
        if not self.circuito_actual.cronos:
            print("NO HAY CRONOS PARA BORRAR.")
        else:
            id_buscado = input("Ingrese el ID del crono a eliminar: ")
            if id_buscado not in self.circuito_actual.cronos:
                print("\n\tERROR! El ID Proporcionado no existe.\n")
            else:
                crono_buscado = self.circuito_actual.cronos[id_buscado]
                print(f"El crono con ID : {id_buscado} es:\n{crono_buscado}")
                while True:
                    confirmacion = input("Desea borrar el crono (si / no)? ").lower()
                    if confirmacion == "si":
                        del self.circuito_actual.cronos[id_buscado]
                        print("SE HA BORRADO EL CRONO.")
                        break
                    elif confirmacion == "no":
                        print("REGRESANDO AL MENU CIRCUITO SIN BORRAR NADA.")
                        break
                    else:
                        print("Input incorrecto, se necesita confirmar o negar con si o no. Vuelva a intentarlo.")

    def salir_menu_circuito(self):
        self.quiere_salir_circuito = True
        print("\nVolviendo al menú principal...")
    # FIN Funciones del menu ciruito

    #Funciones que se hacen en el menu
    def ver_circuitos(self):
        if not self.circuitos:
            print("NO HAY CIRCUITOS PARA VER")
        else:
            print("Lista de Circuitos:")
            for id, circuto in self.circuitos.items():
                print(f"ID: {id}.____{circuto.nombre}\n")
    
    def seleccionar_circuito(self):
        if not self.circuitos:
            print("NO HAY CIRCUITOS PARA SELECCIONAR")
        else:
            id_buscado = input("Ingrese el ID del circuito a seleccionar: ")
            if id_buscado not in self.circuitos:
                print("\n\tERROR! El ID Proporcionado no existe.\n")
            else:
                self.circuito_actual = self.circuitos[id_buscado]
                self.quiere_salir_circuito = False
                while not self.quiere_salir_circuito:
                    self.mostrar_opciones(self.opciones_circuito)
                    opcion = self.ingresar_opcion(self.opciones_circuito) 
                    self.manejar_opcion(opcion, self.opciones_circuito)

    def añadir_circuito(self):
        while True:
            try:
                nombre_circuito_nuevo = input("Ingrese el nombre del circuito: ").strip()
                if not nombre_circuito_nuevo:
                    print("El nombre no puede estar vacío.")
                    continue

                for circuito in self.circuitos.values():
                    if circuito.nombre.lower() == nombre_circuito_nuevo.lower():
                        raise CircuitosNombresIguales()
                break  
            except CircuitosNombresIguales as e:
                print(f"ERROR: {e}")
        while True:
            try:
                num_curvas = int(input("Ingrese el numero de curvas del circuito, para omitir escriba un numero menor o igual a cero: "))
                if num_curvas <= 0:
                    num_curvas = "No especificado"
                break
            except ValueError as e:
                print(f"ERROR: Ingrese un numero valido {e}")
        while True:
            try:
                distancia = int(input("Ingrese la distancia del circuito, para omitir escriba un numero menor o igual a cero: "))
                if distancia <= 0:
                    distancia = "No especificado"
                break
            except ValueError as e:
                print(f"ERROR: Ingrese un numero valido {e}")
        ubicacion = input("Ingrese la ubicación del circuito, para omitir solo presione enter: ")
        if ubicacion == "":
            ubicacion = "No especificado"
        nuevo_circuito = Circuito(nombre_circuito_nuevo, num_curvas, distancia, ubicacion)
        self.circuitos[nuevo_circuito.id_circuito] = nuevo_circuito

        print("\n\tSe creo y añadio el nuevo circuito\n")
        self.ver_circuitos()

    def borrar_circuito(self):
        if not self.circuitos:
            print("NO HAY CIRCUITOS PARA BORRAR.")
        else:
            id_buscado = input("Ingrese el ID del circuito a eliminar: ")
            if id_buscado not in self.circuitos:
                print("\n\tERROR! El ID Proporcionado no existe.\n")
            else:
                circuito_buscado = self.circuitos[id_buscado]
                print(f"El circuito con ID : {id_buscado} es:\n{circuito_buscado}")
                while True:
                    confirmacion = input("Desea borrar el circuito y todos sus registros (si / no)? ").lower()
                    if confirmacion == "si":
                        del self.circuitos[id_buscado]
                        print("SE HA BORRADO EL CIRCUITO Y SUS REGISTROS.")
                        self.ver_circuitos()
                        break
                    elif confirmacion == "no":
                        print("REGRESANDO AL MENU SIN BORRAR NADA.")
                        break
                    else:
                        print("Input incorrecto, se necesita confirmar o negar con si o no. Vuelva a intentarlo.")

    def salir_menu(self):
        print("\n", "SALIENDO DEL PROGRAMA.".center(70,"-"))
        print("ADIOS MUNDO.")
        self.quiere_salir = True
    #Fin funciones que se hacen en el menu

    def guardar_datos(self, archivo="datos.json"):
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.circuitos.items()}, f, indent=4)
        print("Datos guardados en JSON.")
    
    def cargar_datos(self, archivo="datos.json"):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.circuitos = {k: Circuito.from_dict(v) for k, v in data.items()}
            print("Datos cargados desde JSON.")
        except FileNotFoundError:
            print("No hay archivo JSON. Se inicia con datos vacíos.")

    @property
    def opciones(self):
        return self._opciones
    
    @property
    def opciones_circuito(self):
        return self._opciones_circuito
    
def debug():
    # Crear un circuito de prueba
    circuito = Circuito("Nürburgring", 154, 20832, "Alemania")
    
    # Crear un coche y una moto de prueba
    coche = Coche("Toyota GR Supra", "RWD", "Michelin Pilot Sport")
    moto = Moto("Yamaha R1", "Pirelli Diablo Rosso")

    # Crear tiempos para ambos
    tiempo_coche = Tiempo(7, 32, 0.856)  # 7:32.856
    tiempo_moto = Tiempo(8, 15, 0.321)   # 8:15.321

    # Crear cronos
    crono1 = Crono(coche, tiempo_coche)
    crono2 = Crono(moto, tiempo_moto)

    # Añadir cronos al circuito
    circuito.añadir_crono(crono1)
    circuito.añadir_crono(crono2)

    # Imprimir resultados
    print("MOSTRANDO CIRCUITO CON CRONOS DE PRUEBA:")
    print(circuito)


if __name__ == "__main__":
    debug()