import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


load_dotenv()

# export SPOTIPY_CLIENT_ID='8c425a2e376846f0b3d53d8d4fa9a9a0'
# export SPOTIPY_CLIENT_SECRET='97aac6d4b18341d1b81aacb9f1fe04cd'
# export SPOTIPY_REDIRECT_URI='http://localhost/'

client_id = "8c425a2e376846f0b3d53d8d4fa9a9a0"
client_secret = "97aac6d4b18341d1b81aacb9f1fe04cd"

metallica_uri = 'spotify:artist:1a2b3c4d5e6f7g2ye2Wgw4gimLv2eAKyk1NB?si=T3WOLkgZSiispl0oV5TO2Q'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id,client_secret=client_secret ))

results = spotify.artist_albums(metallica_uri, album_type='album')

albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])


