import csv
import json

# Nombre del archivo CSV que queremos convertir
archivo_csv = 'data/games.csv'

# Nombre del archivo JSON de salida
archivo_json = 'data/games.json'

# Leer el archivo CSV y almacenarlo como un diccionario
with open(archivo_csv, mode='r', encoding='utf-8') as csv_file:
    # Usamos el método DictReader para leer el CSV como diccionarios
    csv_reader = csv.DictReader(csv_file)
    
    # Convertimos los datos a una lista de diccionarios
    juegos = []
    for fila in csv_reader:
        # Dividir la columna 'moves' para obtener las primeras dos jugadas
        jugadas = fila['moves'].split()[:2]
        if len(jugadas) == 2:
            # Convertir el valor de 'winner' a un formato de resultado
            if fila['winner'] == 'white':
                resultado = '1-0'
            elif fila['winner'] == 'black':
                resultado = '0-1'
            else:
                resultado = '1/2-1/2'
            
            juego = {
                "moves": jugadas,
                "result": resultado,
                "white_rating": fila['white_rating'],
                "black_rating": fila['black_rating'],
                "increment_code": fila['increment_code']
            }
            juegos.append(juego)

# Escribir los datos en un archivo JSON
with open(archivo_json, mode='w', encoding='utf-8') as json_file:
    # Convertir la lista de diccionarios a formato JSON
    json.dump(juegos, json_file, indent=4, ensure_ascii=False)

print(f'Archivo {archivo_json} creado exitosamente.')