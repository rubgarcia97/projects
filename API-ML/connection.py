import requests
import pandas as pd

from environment import Environment

environment = Environment()

#Creamos carpeta donde se alojaran nuestras peticiones
environment.create_folder("files")

#Configuración básica de la API
base_url="https://www.fema.gov/api/open/v2/"
endpoint="DisasterDeclarationsSummaries"
params={
    '$top':10
}

url=base_url+endpoint


#Requests
response = requests.get(url, params=params)
json_content = response.json()["DisasterDeclarationsSummaries"]
environment.create_file("Prueba",json_content)


df = pd.read_json('./files/Prueba')

df.to_csv('archivo.csv', index=False)