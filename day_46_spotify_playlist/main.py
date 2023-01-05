from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth   # authenticating with spotify
import os

URL = "https://www.billboard.com/charts/hot-100/"

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = "https://example.com/callback"

# >>>>>>>>>>>>>>>>>>> asking the user for date <<<<<<<<<<<<<<<<<<<<<<<

time_travel_date = input("Which year do you want to travel to?\nEnter the date in this format YYYY-MM-DD: ")

# url is modified with this date

# >>>>>>>>>>>>>>>>>>>>>>> scrapping billboard webpage for song names <<<<<<<<<<<<<<<<<<<<<<

response = requests.get(URL+time_travel_date)
response.raise_for_status()
top_playlist_webpage = response.text


soup = BeautifulSoup(top_playlist_webpage, "html.parser")

# all_songs = soup.select("li ul li h3")  # using css selectors
all_songs = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
all_titles = [song.getText().strip("\n\t") for song in all_songs]

# print(all_titles)

# >>>>>>>>>>>>>>>>>>>>>>>  Authentication with spotify <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# after confirming the username copy and paste the redirect url to terminal
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
# get the user id of the current authenticated user
user_id = sp.current_user()["id"]

# >>>>>>>>>>>>>>>>>>>>>>>> Search spotify for thr songs from the list of top 100 songs <<<<<<<<<<<<<<<

song_uri = []  # uri is an identifier used by spotify
year = time_travel_date.split("-")[0]  # taking the year alone to narrow down our search

for song in all_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)

# if the song is available append the uri to a list else skip the song
    try:
        uri = result["tracks"]["items"][0]["uri"]  # find the uri for all songs from the result
        song_uri.append(uri)
    except IndexError:
        print(f"{song} is not available in spotify, skipped.")


# Create a new private playlist with the name "YYYY-MM-DD Billboard 100", where the date is the date we set at the start
playlist = sp.user_playlist_create(user=user_id, name=f"{time_travel_date} Billboard 100", public=False)

# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)  # adding the tracks to playlist
