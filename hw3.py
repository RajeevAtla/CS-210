#--- PART 1: READING DATA ---

# 1.1
def read_ratings_data_master(f):
    ratings_data, contents = {}, None

    with open(f, 'r') as file_obj:
        contents = file_obj.read()

    for line in contents.split('\n'):
        try:
            movie_name, rating, user_id = line.split('|')
        except:
            continue

        if movie_name not in ratings_data.keys():
            ratings_data[movie_name] = []
        ratings_data[movie_name].append((int(user_id), float(rating)))

    return ratings_data

def read_ratings_data(f):
    unfiltered = read_ratings_data_master(f)
    return {key:[val[-1] for val in value] for (key, value) in unfiltered.items()}

# 1.2
def read_movie_genre(f):
    genre_data, contents = {}, None

    with open(f, 'r') as file_obj:
        contents = file_obj.read()

    for line in contents.split('\n'):
        try:
            genre, movie_id, movie_title = line.split('|')
        except:
            continue

        genre_data[movie_title] = genre

    return genre_data


# --- PART 2: PROCESSING DATA ---

# 2.1
def create_genre_dict(d):
    genre_dict = {}

    for movie, genre in d.items():
        if genre not in genre_dict.keys():
            genre_dict[genre] = []
        genre_dict[genre].append(movie)

    return genre_dict

# 2.2
def calculate_average_rating(d):
    ans = {key:sum(value)/len(value) for (key, value) in d.items()}
    return ans

# --- PART 3: RECOMMENDATION ---

# 3.1
def get_popular_movies_master(d):
    ans = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return ans

def get_popular_movies(d, n = 10):
    ans = get_popular_movies_master(d)
    if len(ans) < n:
        return dict(ans)
    return dict(ans[:n])


# 3.2
def filter_movies(d, thres_rating = 3):
    ans = {key:value for (key, value) in d.items() if value >= thres_rating}
    return ans

# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n = 5):
    movies = set(genre_to_movies[genre])
    movies = {key:value for (key, value) in
              get_popular_movies_master(movie_to_average_rating) if key in movies}
    return get_popular_movies(movies, n)


# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    movies = genre_to_movies[genre]
    return sum(movie_to_average_rating[movie] for movie in movies)/len(movies)

# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n = 5):
    ans = {genre:get_genre_rating(genre, genre_to_movies, movie_to_average_rating)
           for (genre, movie) in genre_to_movies.items()}
    ans = get_popular_movies(ans, n)
    return ans

# --- PART 4: USER FOCUSED ---
# 4.1
def read_user_ratings(f):
    data = read_ratings_data_master(f)
    ans = {}

    for movie, ratings in data.items():
        for rating in ratings:
            user = rating[0]
            score = rating[-1]

            if user not in ans.keys():
                ans[user] = []
            ans[user].append((movie, score))

    return ans

# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    ratings = user_to_movies[user_id]
    ratings = [(movie_to_genre[rating[0]], rating[1]) for rating in ratings]
    ratings = sorted(ratings, key = lambda x: x[1])

    return ratings[0][0]

# 4.3
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    top_genre = get_user_genre(user_id, user_to_movies, movie_to_genre)
    rated_movies = [rating[0] for rating in user_to_movies[user_id]]
    all_movies = create_genre_dict(movie_to_genre)[top_genre]
    movies = set(all_movies).difference(set(rated_movies))
    movies = {movie:rating for (movie, rating) in movie_to_average_rating.items()
              if movie in movies}
    return get_popular_movies(movies, 3)
