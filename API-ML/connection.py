import json
import os
import math
import pandas as pd
import requests

from datetime import datetime
from environment import Environment

environment = Environment()

#Rutas que utilizaremos
content_dir = 'src/files'
file_name = 'DisasterDeclarationsSummaries'
full_path = os.path.join(content_dir, file_name)
environment.create_folder(content_dir)


# Configuración básica de la API, al estar esta limitada a 1000 resultado por petición,
base_url = "https://www.fema.gov/api/open/v2/"
endpoint = "DisasterDeclarationsSummaries"
params = {
    "$orderby": "declarationDate desc",
}
url = base_url + endpoint





#Hacemos una petición para conocer el numero de resultados totales que se disponen
top=1000
skip=0

response = requests.get(url,params="$inlinecount=allpages&$select=id&$top=1")
registres = response.json()['metadata']['count']

n_loop = math.ceil(registres/top) #Peticiones necesarias





#Petición lanzada desde un bucle while 

print('START:'+str(datetime.now())+f' se realizaran {n_loop} ({registres} registros disponibles) llamadas a la API de {url}')

data = []  # Creamos un array vacío para almacenar los objetos JSON

i = 0
while (i < n_loop):
    response = requests.get(url, params= "&$metadata=off&$format=jsona&$skip=" + str(skip) + "&$top=" + str(top))
    content = response.json()
    data.extend(content)  # Agregamos cada objeto JSON al array
    i += 1
    skip = 1 * top

    print("iteration " +str(i) + " done")

outFile = open(full_path+'.json', "w")  # Usamos el modo 'w' para sobrescribir el archivo
outFile.write(json.dumps(data))  # Escribimos todo el array en el archivo
outFile.close()





#Comprobación de los registros grabados
inFile = open(full_path + '.json', 'r')
data = json.load(inFile)
print("END: " + str(datetime.now()) + ',' + str(len(data)) + 'records in file')
inFile.close()




# cargar los datos desde el archivo JSON
with open(full_path+'.json', 'r') as f:
    data = json.load(f)

# crear el DataFrame a partir de la lista de datos
df = pd.DataFrame(data)

# guardar el DataFrame en un archivo CSV
csv_filename = full_path+'.csv'
df.to_csv(csv_filename, index=False)
