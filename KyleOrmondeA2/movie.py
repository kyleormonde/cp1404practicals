"""
CP1404: Assignment 2
Movie Class
"""


# create your Movie class in this file


class Movie:
    """Represents a Movie object"""
    def __init__(self, title="", year=0, category="", is_watched=False):
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched

    def __str__(self):
        return "{}".format(self.title)

    def mark_required(self):
        self.is_watched = False

    def mark_watched(self):
        self.is_watched = True
