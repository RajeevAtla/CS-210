from hw3 import *
from pprint import pprint

genre_url = "genreMovieSample.txt"
rating_url = "movieRatingSample.txt"

genres = read_movie_genre(genre_url)
ratings = read_ratings_data(rating_url)
ratings_average = calculate_average_rating(ratings)
genre_to_movies = create_genre_dict(genres)
user_ratings = read_user_ratings(rating_url)

pprint(recommend_movies(1, user_ratings, genres, ratings_average))
