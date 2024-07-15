import os
import requests

def descargar_proyecto(identificador):
    url = f"https://api.scratch.mit.edu/projects/{identificador}/"
    response = requests.get(url)
    if response.status_code == 200:
        proyecto = response.json()
        # Guarda el proyecto como archivo JSON
        nombre_archivo = f"proyecto_{identificador}.json"
        ruta_guardado = os.path.join("proyectos_descargados", nombre_archivo)
        with open(ruta_guardado, "w") as archivo:
            archivo.write(str(proyecto))
        print(f"Descargando proyecto {identificador}: {proyecto['title']}")
    else:
        print(f"Error al descargar proyecto {identificador}")

# Crea la carpeta para almacenar los proyectos descargados
if not os.path.exists("proyectos_descargados"):
    os.makedirs("proyectos_descargados")

# Lee los identificadores desde el archivo de texto
with open("batch_master_id.txt", "r") as archivo:
    for linea in archivo:
        identificador = linea.strip()  # Elimina espacios y saltos de línea
        descargar_proyecto(identificador)
