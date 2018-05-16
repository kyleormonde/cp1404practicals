"""(Incomplete) Tests for Movie class."""
from movie import Movie


def run_tests():
    """Test Movie class."""
    # Test empty movie (defaults)
    movie = Movie()
    print(movie)
    assert movie.title == ""
    assert movie.year == 0
    assert movie.category == ""
    assert not movie.is_watched

    # Test initial-value movie
    movie2 = Movie("Thor: Ragnarok", 2017, "Comedy", True)
    # TODO: write tests to show this initialisation works
    print(movie2)

    # test mark_required()
    # TODO: write tests to show the mark_required() method works
    movie.mark_required()
    assert not movie.is_watched

    # TODO: more tests, as appropriate
    movie.mark_watched()
    assert movie.is_watched


run_tests()
