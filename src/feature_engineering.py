import numpy as np

movie_metadata = []

def normalize_feature(value, min, max, scaled_min=0, scaled_max=1):
    return ((value - min) / (max - min)) * (scaled_max - scaled_min) + scaled_min

def load_movie_cache():
    import csv
    movie_data = []
    with open('data/raw/movie_cache.csv', 'r', encoding="utf-8") as cache_file:
        reader = csv.DictReader(cache_file)
        for row in reader:
            movie_data.append(row)
    return movie_data

def load_ratings():
    import csv
    ratings = []
    with open('data/raw/ratings.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ratings.append(row['Rating'])
    return ratings

def transform(movie_data):
    from data.constants import GENRE_LIST, TOP_DIRECTORS, TOP_ACTORS

    # Multi-hot encoding for genres
    genre_multi_hot = [0] * len(GENRE_LIST)
    movie_genres = movie_data['Genre'].split(', ')

    for genre in GENRE_LIST:
        if genre in movie_genres:
            genre_multi_hot[GENRE_LIST.index(genre)] = 1

    # Multi-hot encoding for actors
    actors_multi_hot = [0] * len(TOP_ACTORS)
    movie_actors = movie_data['Actors'].split(', ')

    for actor in TOP_ACTORS:
        if actor in movie_actors:
            actors_multi_hot[TOP_ACTORS.index(actor)] = 1

    # One-hot encoding for directors
    director_one_hot = [0] * len(TOP_DIRECTORS)
    if movie_data['Director'] in TOP_DIRECTORS:
        director_one_hot[TOP_DIRECTORS.index(movie_data['Director'])] = 1
    
    # Normalizing numerical features
    normalized_runtime = normalize_feature(int(movie_data['Runtime'].replace(' min', '')), 60, 300)
    normalized_rating = normalize_feature(float(movie_data['imdbRating']), 0, 10)

    return [*genre_multi_hot, *actors_multi_hot, *director_one_hot, normalized_runtime, normalized_rating]

def process_data():
    movie_metadata = load_movie_cache()
    xArr = [transform(movie) for movie in movie_metadata]
    yArr = load_ratings()
    return xArr, yArr

# def cache_processed_data():    
#     np.save("data/processed/X.npy", xArr)
#     np.save("data/processed/y.npy", yArr)

# xArr, yArr = process_data()
# cache_processed_data()
