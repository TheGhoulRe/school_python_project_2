import requests
import json
import matplotlib.pyplot as plt
import numpy as np

def search_movie(search_bar, listbox):
    movie_name = search_bar.get("1.0", "end-1c").replace(" ", "+")
    movies = get_movies(movie_name)
    genres = get_genres(movies)
    display_genres(genres, listbox)

def show_pie_chart(search_bar):
    movie_name = search_bar.get("1.0", "end-1c").replace(" ", "+")
    movies = get_movies(movie_name)
    genres = get_genres(movies)
    genre_names = genres.keys()
    genre_counts = np.array( [ genres[name] for name in genre_names] )
    
    plt.pie(genre_counts, labels=genre_names)
    plt.show()


def get_movies(movie_name):
    response = requests.get(f"http://www.omdbapi.com/?apikey=2af385ca&s={movie_name}")
    return json.loads( response.text )["Search"]

def get_genres(movies):
    movie_IDs = [ movie["imdbID"] for movie in movies ]
    genres = {}

    for id in movie_IDs:
        movie_genres = get_movie_genres(id)
        for genre in movie_genres:
            if genre in genres:
                genres[genre] += 1
            else:
                genres[genre] = 1
    
    return genres

def get_movie_genres(id):
    response = requests.get(f"http://www.omdbapi.com/?apikey=2af385ca&i={id}")
    obj = json.loads( response.text )
    genres = obj["Genre"].split(", ")
    return genres

def display_genres(genres, listbox):
    text = "{genre} - {count}"

    for genre in genres.keys():
        listbox.insert("end", "")
        listbox.insert("end", text.format(genre=genre, count=genres[genre]) )
        listbox.insert("end", "")
