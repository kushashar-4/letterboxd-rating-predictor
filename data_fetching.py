import requests
from data.constants import OMDB_API_KEY
import csv

def cache_movie_metadata():
    data = []
    with open('data/ratings.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(fetch_movie_metadata(row['Name'], row['Year']))
    
    with open('data/movie_cache.csv', 'w', newline="", encoding="utf-8") as cache_file:
        writer = csv.DictWriter(cache_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def fetch_movie_metadata(movie_name, movie_year):
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={movie_name}&y={movie_year}"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: {response.status_code}")