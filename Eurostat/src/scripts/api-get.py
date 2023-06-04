import requests
import json

#BASE URL
base_url_ESTAT = 'https://ec.europa.eu/eurostat/api/dissemination'
base_url_COMP = 'https://webgate.ec.europa.eu/comp/redisstat/api/dissemination'
base_url_EMPL = 'https://webgate.ec.europa.eu/empl/redisstat/api/dissemination'
base_url_GROW = 'https://webgate.ec.europa.eu/grow/redisstat/api/dissemination'


#CATALOGUE ENDPOINTS: Only in COMP,EMPL and GROW
CATALOGUE_ENDP = '/catalogue/catalogue.wadl'

#SDMX 2.1 PROTOCOL
SDMX_ENDP = '/sdmx/2.1/sdmx-rest.wadl'


url = base_url_ESTAT + SDMX_ENDP

response = requests.get(url)

print(response.status_code)

