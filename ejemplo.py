"""
    Eric Pasto i Matteo Vilchez.
    30/04/2024
    ASIXc 1B  M03 UF3 A1
    ParaulesBoges Pt.3
    Implementa un arxiu de entrada, log i un arxiu de sortida tot senza menu
"""
FILE_NAME = "paraules.txt"
import random
cEspeciales = [".", ",", "?", ":", ";", "!", "'", "¡", "¿"]
Texto_Ordenado=[]
palabras=[]
frase_Desordenado=[]

def leerParaules():
    with open(FILE_NAME, mode='r', encoding='UTF-8') as fichero:
        contenido = fichero.read()
        print(contenido)

leerParaules()
