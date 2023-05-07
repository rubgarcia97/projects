import json
import os
import math
import pandas as pd
import requests

from environment import Environment

environment = Environment()

content_dir = 'src/files'
file_name = 'DisasterDeclarationsSummaries'
full_path = os.path.join(content_dir, file_name)

# Configuración básica de la API, al estar esta limitada a 1000 resultado por petición,
# hacemos una petición para conocer el numero de resultados totales que se disponen
base_url = "https://www.fema.gov/api/open/v2/"
endpoint = "DisasterDeclarationsSummaries"
params = {
    "$orderby": "declarationDate desc",
    "$inlinecount": "allpages",
    "$select": "id",
    "$top": 1,
}

url = base_url + endpoint

response = requests.get(url, params=params)
json_content = response.json()["metadata"]["count"]

n_loop = math.ceil(json_content / 1000)

# Generamos mediante un bucle tantas peticiones como son necesarias para traer toda la información

environment.create_folder(content_dir)


skip = 0
top = 1000

outFile = open(full_path+".json", "a")
# outFile.write('{"femawebdisasterdeclarations":[')

i = 0
while (i < n_loop):
    response = requests.get(url, params="&$metadata=off&$format=jsona&$skip=" + str(skip) + "&$top=" + str(top))
    json_content = response.json()

    if i == (n_loop - 1):
        outFile.write(json.dumps(json_content[1:-1]) + "]")
    else:
        outFile.write(json.dumps(json_content[1:-1]) + ",")

    i += 1
    skip = i * 1000

outFile.close()


df = pd.read_json(full_path+'.json')
df.to_csv(content_dir+'/'+file_name+'.csv', index=False)