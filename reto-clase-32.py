import csv
import json

# Traductor de archivo CSV con headers a JSON
with open('original.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Convierte el lector de CSV en un diccionario de objetos, donde la primera fila corresponde al nombre de cada atributo de los objeto y el resto de fila corrresponde a los valoresprint(list(csv_reader))
    filas = list(csv_reader)
    
    with open('new.json', 'w') as json_file:
        json.dump(filas, json_file, indent = 4)
    
# Traductor de archivo JSON a CSV con headers
with open('original.json', 'r') as json_file:
    products = json.load(json_file)
        
    with open('new.csv', 'w', newline = '') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames = products[1].keys())

        csv_writer.writeheader()
        csv_writer.writerows(products)

