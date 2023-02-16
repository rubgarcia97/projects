import requests


class Petitions():

    def __init__(self):
        pass

    def __response_model(self,base_url,endpoint,headers,params=None,id_source=""):
        
        response = requests.get(base_url+endpoint+id_source, headers = headers, params=params)
        json_response = response.json()

        return json_response

    def get_artist(self,base_url,headers,limit):
        
        json_response = Petitions().__response_model(base_url,"me/top/artists",headers)
        content = [json_response['items'][i]['name'] for i in range(limit)]

        return {"Artist" : content}

    def get_tracks(self,base_url,headers,params):

        json_response = Petitions().__response_model(base_url,"me/top/tracks",headers,params)

        content_tracks = [json_response['items'][i]['name'] for i in range(params['limit'])]
        content_artist = [json_response['items'][i]['artists'][0]['name'] for i in range(params['limit'])]

        content_mix = {content_tracks[i] : content_artist[i] for i in range(params['limit'])}

        return content_mix

    def get_genres(self,base_url,headers,limit):

        json_response = Petitions().__response_model(base_url,"me/top/artists",headers)
        content = [json_response['items'][i]['genres'][0] for i in range(limit)]

        return {"Genres" : content}

    def get_cover_image(self,base_url,headers,params,id_source):
        """
        Get cover image from a spotify playlist
        """

        json_response = Petitions().__response_model(base_url,"playlists/",headers,params,id_source)
        url = json_response['images'][0]['url']

        return requests.get(url).content

    def get_followers(self,base_url,headers,params,id_source):

        """
        Get total followers from a spotify playlist
        """

        json_response = Petitions().__response_model(base_url,"playlists/",headers,params,id_source)

        return {"followers" : json_response['followers']['total']}

    def get_metrics(self,base_url,headers,params,id_source,metrics):

        """
        Get metrics from a track list
        """

        json_response = Petitions().__response_model(base_url,"playlists/",headers,params,id_source)

        aux = []
        for track in range(len(json_response['tracks']['items'])):
            params_metric = {
                'ids' : str(json_response['tracks']['items'][track]['track']['id'])
            }
            
            response = requests.get(base_url+'audio-features', headers=headers,params=params_metric)
            json_response_metrics = response.json()

            kpi = metrics
            content_kpi_tracks = json_response['tracks']['items'][track]['track']['name']
            content_kpi ={i : json_response_metrics['audio_features'][0][i] for i in kpi}

            content_mix = {content_kpi_tracks : content_kpi}
            aux.append(content_mix)

        return aux

        
