from Vehiculo import Coche, Moto
from Tiempo import Tiempo
from Crono import Crono
from Circuito import Circuito
from Menu import Menu
import os

ruta_base = os.path.dirname(__file__)
ruta_crono = os.path.join(ruta_base, "crono.txt")
quiere_salir = False

menu = Menu()
menu.cargar_datos()

try:
    with open(ruta_crono, "r", encoding="utf-8") as crono:
        print(crono.read())
except FileNotFoundError:
    print("(No se encontró el archivo crono.txt)")
print("TIEMPOS DE VUELTA POR CIRCUITO".center(70,"-"))

while not menu.quiere_salir:
    menu.mostrar_opciones(menu.opciones)
    opcion = menu.ingresar_opcion(menu.opciones)
    menu.manejar_opcion(opcion, menu.opciones)
    
menu.guardar_datos()
