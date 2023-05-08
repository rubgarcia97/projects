import json
import os
import math
import pandas as pd
import requests

from datetime import datetime
from environment import Environment

environment = Environment()

content_dir = 'src/files'
file_name = 'DisasterDeclarationsSummaries'
full_path = os.path.join(content_dir, file_name)

# environment.create_folder(content_dir)

# Configuración básica de la API
base_url = "https://www.fema.gov/api/open/v2/"
endpoint = "DisasterDeclarationsSummaries"
url = base_url + endpoint

#Peticiones necesarias
top=1000
skip=0

response = requests.get(url,params="$inlinecount=allpages&$select=id&$top=1")
registres = response.json()['metadata']['count']

n_loop = math.ceil(registres/top)
print('START:'+str(datetime.now())+f' se realizaran {n_loop} llamadas a la API de {url}')


