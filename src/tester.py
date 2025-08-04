from data_fetching import fetch_movie_metadata
from feature_engineering import transform

info = fetch_movie_metadata("Cars", "2006")
infoVector = transform(info)

print(infoVector)