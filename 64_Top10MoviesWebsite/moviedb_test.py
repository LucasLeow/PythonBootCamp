import requests
import os

bearer_token = os.environ['BEARER']
url = "https://api.themoviedb.org/3/search/movie"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {bearer_token}"
}

movie_params = {
    'query': 'The Matrix',
    'include_adult': False,
    'language': 'en-US',
    'page': 1
}

response = requests.get(
    url,
    headers=headers,
    params=movie_params
)

all_movies = response.json()['results']

print(len(all_movies))
print(all_movies)