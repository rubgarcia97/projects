import os

from environment import Environment
from petitions import Petitions
from auth import Auth

base_url = 'https://api.spotify.com/v1/'
playlist = "37i9dQZF1DWWGFQLoP9qlv"

auth = Auth()
environment = Environment()
petitions = Petitions()

auth.generate_token()    # use it only for the first time
token = auth.get_token()

headers = {
    'Authorization': f'Bearer {token}',
    "Accept": "application/json"
}

params = {
    'limit' : 10,
    'time_range' : 'short_term'
}

environment.create_folder("Spotify Wrapped of {}".format(os.getlogin()))


## Top 10 artist

artist = petitions.get_artist(base_url,headers,limit=10)
environment.create_file("Top Artist.json", artist)


## Top 10 tracks 


tracks = petitions.get_tracks(base_url,headers,params)
environment.create_file("Top Tracks.json", tracks)

## Top Genres

genre = petitions.get_genres(base_url,headers,limit=5)
environment.create_file("Top Genres.json", genre)

##Playlist

params_playlist = {
    'additional_types' : 'track',
    'fields' : 'followers,images'
}

## Save image

image = petitions.get_cover_image(base_url,headers,params_playlist,id_source=playlist)
environment.create_image('Playlist_image.jpg', image)

##Followers

followers = petitions.get_followers(base_url,headers,params_playlist,id_source=playlist)
environment.create_file("Playlist_Followers.json", followers)

## METRICS

params_kpi = {
    'additional_types' : 'track',
    'fields' : 'tracks.items(track(id,name))'
}
kpi = ['tempo','acousticness','danceability','energy','instrumentalness','liveness','loudness','valence']

metrics = petitions.get_metrics(base_url,headers,params_kpi,id_source=playlist,metrics=kpi)
environment.create_file('Playlist_Metrics.json', metrics)

