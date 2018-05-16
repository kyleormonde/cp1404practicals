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
    print("by category:")
    movie_list.sort("category")
    print(movie_list)

    print("by is watched:")
    movie_list.sort("is_watched")
    print(movie_list)

    # TODO: Test saving movies (check CSV file manually to see results)
    movie_list.save_movies()

    # TODO: Test getting the number of required and watched movies (separately)
    print("Get number of watched / required (expect 6 total):")
    print(movie_list.get_number_watched())
    print(movie_list.get_number_required())
    # Expect total of 6

    # TODO: more tests, as appropriate
    

run_tests()
