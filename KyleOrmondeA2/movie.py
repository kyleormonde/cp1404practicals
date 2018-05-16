"""
Movie Class
"""


# create your Movie class in this file


class Movie:
    """Represents a Movie object"""
    def __init__(self, title="", year=0, category="", is_watched):
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched

    def __str__(self):
        
