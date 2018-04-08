"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""


def main():
    title = 'The Godfather'
    year = 0
    category = 'Drama'
    year = check_movie_year()
    print("{} ({} from {}) added to movie list".format(title, category, year))


def check_movie_year():
    finished = False
    while not finished:
            try:
                year = int(input("Year: "))
                if year <= 0:
                    print("Number must be >= 0")
                else:
                    finished = True
                    return year
            except ValueError:
                print("Please enter a valid integer.")
            except TypeError:
                print("Please enter a valid type.")






main()










    # finished = False
    # new_movie = []
    # while not finished:
    #     try:
    #         title = input("Title: ")
    #         year = int(input("Year: "))
    #         category = input("Category: ")
    #         print("{} ({} from {}) added to movie list".format(title, category, year))
    #         new_movie = [title, year, category, 'n']
    #         finished = True
    #     except ValueError:
    #         print("Invalid value")
    #     except TypeError:
    #         print("Invalid type")
