from os import system
import sys
from enum import Enum

def borrar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        system("clear")
    else:
        system("cls")

def pausar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        x=input("Presione una tecla para continuar")
    else:
        system("pause")

Pancam_compra = {
    "data_Compras" : {}
}