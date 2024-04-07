from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# year = input("What year would you like ot travel to?(YYYY-MM-DD): ")
year = "2024-02-19"
site = f"https://www.billboard.com/charts/hot-100/{year}/"
response = requests.get(site).text
soup = BeautifulSoup(response, "html.parser")
song_titles = soup.select("li ul li h3")
songs = [song.getText().strip() for song in song_titles]

CLIENT_ID = "051bb89f90964f5abd2c0cfa7099cea5"
CLIENT_SECRET = "cdcbf71714d84de2b0d98c931553bc04"
OAUTH_AUTHORIZE_URL= 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL= 'https://accounts.spotify.com/api/token'


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Cece",
    )
)
user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

