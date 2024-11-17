import os
import argparse
#print(os.name)
#print(os.environ)
#os.mkdir("testdir")
parser = argparse.ArgumentParser(description="Script que encuentra texto en un fichero")

# Definir los argumentos
#parser.add_argument("fichero", type=str, help="Nombre del fichero donde guardar el texto")
parser.add_argument("texto", type=str, help="Texto a buscar en el fichero")

# Parsear los argumentos
args = parser.parse_args()

nombre_fichero = "environment.txt"

# Escribir las variables de entorno en el fichero
with open(nombre_fichero, "w", encoding="utf-8") as fichero:
    for clave, valor in os.environ.items():
        fichero.write(f"{clave}: {valor}\n")
    #fichero.write(args.texto)

# Abrir y buscar el texto en el fichero
encontrado = False
with open(nombre_fichero, "r", encoding="utf-8") as fichero:
    for linea in fichero:
        if args.texto in linea:
            print(f"Texto encontrado: {linea.strip()}")
            encontrado = True

if not encontrado:
    print(f"El texto '{args.texto}' no se encontró en el archivo.")

#os.listdir(".")
#os.chdir("/ruta/a/directorio")