def leerParaules():
    with open(FILE_NAME, mode='r', encoding='UTF-8') as fichero:
        contenido = fichero.read()
        print(contenido)

leerParaules()
