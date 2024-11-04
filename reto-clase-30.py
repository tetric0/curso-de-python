# Conteo de las líneas de un archivo de texto
with open('cuento.txt', 'r') as file:
    print("El cuento tiene {} líneas".format(len(file.readlines())))