import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests
from bs4 import BeautifulSoup

# Constants ====================================================================
URL = "https://www.billboard.com/charts/hot-100"

YT_KEY = os.environ['yt_api_key']
YT_PLAYLIST_ID = os.environ['yt_playlist_id']
YT_TOKEN = os.environ['yt_token']
client_secret_file_name = os.environ['client_secret_file_name']

YT_search_endpoint = 'https://www.googleapis.com/youtube/v3/search'
YT_playlist_endpoint = 'https://www.googleapis.com/youtube/v3/playlistItems'

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
api_service_name = "youtube"
api_version = "v3"
client_secrets_file = client_secret_file_name
# Setup  ====================================================================
user_date_input = input(
    "Which year do you want to travel to? Type date in this format: (YYYY-MM-DD): ")

# print(URL + f'/{user_date_input}/')
res = requests.get(URL + f'/{user_date_input}/')
billboard_hot_100_html = res.text

soup = BeautifulSoup(billboard_hot_100_html, 'html.parser')
top_100_songs = []
top_10_songs_video_id = []

# Web Scraping  ==================================================================
song_titles = soup.find_all(
    name="h3",
    class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"
)
for s in song_titles:
    top_100_songs.append(s.getText().replace('\n', '').replace('\t', ''))

print(top_100_songs)
top_10_songs = top_100_songs[:10]

# Search On Youtube  ==================================================================
for song in top_10_songs:
    yt_params = {
        'part': "snippet",
        'key': YT_KEY,
        'type': 'video',
        'q': song,
    }
    yt_res = requests.get(
        url=YT_search_endpoint,
        params=yt_params
    )

    try:
        playlist_data = yt_res.json()['items']
        top_10_songs_video_id.append(playlist_data[0]['id']['videoId'])
        print(f"{playlist_data[0]['id']['videoId']} appended")
    except KeyError:
        print(yt_res.text)
        pass

print(top_10_songs_video_id)
# Add to Youtube Playlist ==================================================================
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
credentials = flow.run_console()
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)

for id in top_10_songs_video_id:
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": YT_PLAYLIST_ID,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": id
                }
            }
        }
    )

    response = request.execute()
    print(f"{id} successfully added")
