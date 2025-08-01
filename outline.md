# Letterboxd Rating Predictor

## Data Collection
- For each of my letterboxd watched movies collect 
    - Title
    - Genre
    - Director
    - Lead actor
    - Year
    - Runtime
    - Average rating
    - Review count
- Data collection
    - [API](https://www.omdbapi.com/)
    - Send get requests with keys being movie titles


## Pre-Processing
- Encoding
    - Genres (multi hot encoding)
    - Director (One-hot based on a list of top 100 directors)
    - Cast (multi hot encoding based on a list of top 100 actors)
    - Year, runtime, avg_rating, review_count (all normalized scalars between 0-1)
    - Total vector length: 214
