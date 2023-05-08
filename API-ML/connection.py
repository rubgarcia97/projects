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

environment.create_folder(content_dir)

# Configuración básica de la API, al estar esta limitada a 1000 resultado por petición,
# hacemos una petición para conocer el numero de resultados totales que se disponen
base_url = "https://www.fema.gov/api/open/v2/"
endpoint = "DisasterDeclarationsSummaries"
params = {
    "$orderby": "declarationDate desc",
}

url = base_url + endpoint

response = requests.get(url, params=params)
json_content = response.json()["DisasterDeclarationsSummaries"]

df = pd.DataFrame(json_content)
csv_filename = full_path+'.csv'
df.to_csv(csv_filename, index=False)