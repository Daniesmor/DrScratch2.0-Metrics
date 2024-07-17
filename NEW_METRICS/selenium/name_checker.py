import os

# Ruta al archivo con los nombres de archivos
archivo_nombres = 'output_checker'

# Directorio donde quieres comprobar los archivos
directorio = './projects_sb3/'

list_dups = [
"Stop Global Warming.sb3",
"World and Climate Changing Game.sb3",
"Save The Trees.sb3",
"Climate Change Game.sb3",
"Climate Control.sb3",
"`.sb3",
"Science Project.sb3",
"Climate Pong.sb3",
"Untitled-3.sb3",
"Climate Clicker.sb3",
"Carbon Clicker.sb3",
"Deforestation Game.sb3",
"Untitled-2.sb3",
"This Sea Level Rise is Terrible.sb3",
"Untitled.sb3",
"Carbon Run.sb3",
"Climate Change Project.sb3",
"Catch the CO2.sb3",
"Co2 Game.sb3",
"Carbon Capture.sb3",
"climate change game.sb3",
"Deforestation.sb3",
]

# Leer los nombres de archivos del archivo
with open(archivo_nombres, 'r') as f:
    nombres_archivos = f.read().splitlines()

# Comprobar si cada archivo existe en el directorio
for nombre in nombres_archivos:
    ruta_completa = os.path.join(directorio, nombre)
    if os.path.isfile(ruta_completa):
        #print(f'El archivo {nombre} existe en el directorio.')
        pass
    else:
    	#if nombre not in list_dups:
        print(f'El archivo {nombre} NO existe en el directorio.')

