"""
    Eric Pasto i Matteo Vilchez.
    30/04/2024
    ASIXc 1B  M03 UF3 A1
    ParaulesBoges Pt.3
    Implementa un arxiu de entrada, log i un arxiu de sortida tot sense menu
"""

import random
import logging
import os

cEspeciales = [".", ",", "?", ":", ";", "!", "'", "¡", "¿"]

def leerParaules(FILE_NAME):
    with open(FILE_NAME, 'r') as f:
        return f.read()

def separar(leerParaules):
    palabras = []
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

def juntar(palabras):
    return ' '.join(palabras)

def resultado(FILE_NAME, frase_Desordenado):
    output_folder = "sortida"
    output_file = os.path.join(output_folder, os.path.basename(FILE_NAME).replace(".txt", "_boges.txt"))
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Crear la carpeta de salida si no existe
    with open(output_file, "w") as f:  # Abrir el archivo en modo escritura
        f.write(frase_Desordenado + '\n')

try:
    logFile = 'boges.log'
    logFormat = '%(asctime)s %(levelname)s %(message)s'
    logLevel = logging.DEBUG
    logMode = 'a'
    logging.basicConfig(level=logLevel, format=logFormat, filename=logFile, filemode=logMode)

    directory = "./entrada"  # Directorio donde se encuentran los archivos .txt
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            FILE_PATH = os.path.join(directory, filename)
            texto_leido = leerParaules(FILE_PATH)
            palabras = separar(texto_leido)
            frase_Desordenado = juntar(palabras)
            resultado(FILE_PATH, frase_Desordenado)

    logging.debug("Procesamiento completado")

except Exception as e:
    logging.error("Error general: %s", str(e))
