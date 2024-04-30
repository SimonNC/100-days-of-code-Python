import requests
from bs4 import BeautifulSoup
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()

import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to ? Type the date in this format YYYY-MM-DD : ")

# date= "1978-04-16"

url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
hits = soup.select(".o-chart-results-list-row-container")
song_names = []

for hit in hits:
    title = hit.select_one(".c-title").getText().strip()
    song_names.append(title)

#pprint(song_names)

song_uris = []
year = date.split("-")[0]





auth_manager=SpotifyOAuth(
        scope=os.getenv("SPOTIPY_SCOPE"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret= os.getenv("SPOTIPY_CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt",
        username=os.getenv("SPOTIFY_USERNAME")
    )

sp = spotipy.Spotify(auth_manager=auth_manager)

user_id = sp.current_user()["id"]
print(user_id)

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)














