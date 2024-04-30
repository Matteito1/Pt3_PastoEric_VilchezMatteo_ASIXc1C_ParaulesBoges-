"""
    Eric Pasto i Matteo Vilchez.
    30/04/2024
    ASIXc 1B  M03 UF3 A1
    ParaulesBoges Pt.3
    Implementa un arxiu de entrada, log i un arxiu de sortida tot sense menu
"""
import random
import logging
FILE_NAME = "paraules.txt"
cEspeciales = [".", ",", "?", ":", ";", "!", "'", "¡", "¿"]
Texto_Ordenado = []
palabras = []
frase_Desordenado = []

def leerParaules(FILE_NAME):
    with open(FILE_NAME, 'r') as f:
        f = f.read()
        return f

def separar(leerParaules):
    for palabrades in leerParaules.split():
        if len(palabrades) >= 3:
            if palabrades[-1] in cEspeciales:
                sep = list(palabrades[1:-1])
                random.shuffle(sep)
                separado = palabrades[0] + ''.join(sep) + palabrades[-1]
            else:
                sep = list(palabrades[1:-2])
                random.shuffle(sep)
                separado = palabrades[0] + ''.join(sep) + palabrades[-2] + palabrades[-1]
        else:
            separado = palabrades
        palabras.append(separado)
    return palabras

def juntar():
    frasedes = ' '.join(palabras)
    return frasedes

def resultado():
    with open("paraules_boges.txt", "w") as f:
        f.write(frase_Desordenado)

texto_leido = leerParaules(FILE_NAME)
palabras = separar(texto_leido)
frase_Desordenado = juntar()
resultado()

logFile = 'boges.log'

logFormat='%(asctime)s %(levelname)s %(message)s'

logLevel= logging.DEBUG

logMode = 'a'


logging.basicConfig(level=logLevel,format=logFormat,filename=logFile,filemode=logMode)


logging.debug("Mensaje de debug")

logging.info("Mensaje informativo")

logging.error("Error no encuentra el archivo")

