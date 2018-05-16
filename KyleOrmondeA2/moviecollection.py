"""
CP1404: Assignment 2
Movie Collection Class
"""
from movie import Movie
from operator import attrgetter

# create your MovieCollection class in this file


class MovieCollection(Movie):
    """Represent a Movie List"""

    def __init__(self):
        self.movies = []

    def __str__(self):
        # return "{}".format(self.movies)
        return str([str(movie) for movie in self.movies])

    def load_movies(self, movie_file_name):
        movies = []
        movie_file_in = open(movie_file_name, 'r')
        for movie in movie_file_in:
            movies.append(list(movie.strip('\n').split(',')))
        movie_file_in.close()

        for movie in movies:
            title = movie[0]
            year = int(movie[1])
            category = movie[2]
            is_watched = movie[3]
            if is_watched == 'y':
                is_watched = True
            else:
                is_watched = False

            self.movies.append(Movie(title, year, category, is_watched))

    def add_movie(self, new_movie):
        self.movies.append(new_movie)

    def get_number_required(self):
        required_movies = 0
        for movie in self.movies:
            if not movie.is_watched:
                required_movies += 1
        return required_movies

    def get_number_watched(self):
        watched_movies = 0
        for movie in self.movies:
            if movie.is_watched:
                watched_movies += 1
        return watched_movies

    def sort(self, sort_by):
        self.movies.sort(key=attrgetter(sort_by, "title"))
