""" (incomplete) Tests for MovieList class."""
from moviecollection import MovieCollection
from movie import Movie


def run_tests():
    """Test MovieCollection class."""
    # Test empty MovieCollection (defaults)
    print("Empty MovieCollection:")
    movie_list = MovieCollection()
    print(movie_list)
    assert not movie_list.movies  # PEP 8 suggests not using len() to test for empty lists
    assert movie_list.get_number_watched() == 0
    assert movie_list.get_number_required() == 0

    # Test loading movies
    print("Loaded movie list:")
    movie_list.load_movies('movies.csv')
    print(movie_list)
    assert movie_list.movies  # assuming CSV file is non-empty, length is non-zero

    # Test adding a new Movie with values
    print("Add new movie:")
    movie_list.add_movie(Movie("Amazing Grace", 2006, "Drama", False))
    print(movie_list)

    # Test sorting movies
    print("Sorting:")
    print("by year:")
    movie_list.sort("year")
    print(movie_list)
    # TODO: add more sorting tests

    # TODO: Test saving movies (check CSV file manually to see results)

    # TODO: Test getting the number of required and watched movies (separately)

    # TODO: more tests, as appropriate


run_tests()
