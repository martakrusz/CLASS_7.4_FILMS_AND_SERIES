from faker import Faker
import random
from tabulate import tabulate
from operator import attrgetter
from datetime import date

fake = Faker()

#Adding Class about movies
 
class Movie:
    def __init__(self, title, publication_year, genre, number_of_watching):
        self.title = title
        self.publication_year = publication_year
        self.genre = genre
        self.number_of_watching = number_of_watching

    def play(self, step=1):
       self.number_of_watching += step

    def __str__(self):
        return f'{self.title} ({self.publication_year})'

    def __repr__(self):
        return f'Movie(title = {self.title}, publication_yeat = {self.publication_year}, genre ={self.genre}, number_of_watching = {self.number_of_watching})'

class Series(Movie):
    def __init__(self, episode_number: int, season_number: int, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f'{self.title} S{self.season_number:02d}E{self.episode_number:02d}'

    def __repr__(self):
        return f'Series(title = {self.title}, publication_yeat = {self.publication_year}, genre ={self.genre}, number_of_watching = {self.number_of_watching}, episode_numer = {self.episode_number}, season_number = {self.season_number})'

# Create a movies and series lists as movies_data

genre_list = ['comedy', 'familly', 'romace', 'horror']

def create_movies():
    for _ in range(5):
        library.append(
                Movie(
                    title = fake.first_name(), 
                    publication_year = fake.random_int(min=1980, max=2020),
                    genre = random.choice(genre_list),
                    number_of_watching = fake.random_int(0,100),
                )
            )
    return library

def create_series():
    for _ in range(5):
        library.append(
                Series(
                    title = fake.first_name(), 
                    publication_year = fake.random_int(min=1980, max=2020),
                    genre = random.choice(genre_list),
                    season_number = fake.random_int(0,24),
                    episode_number = fake.random_int(0,10),
                    number_of_watching = fake.random_int(0,100),
                )
            )
    return library 

def movies_data():
    create_movies()
    create_series()
    return library

# Get movies and series sorted lists

def get_movies():
    for i in library:
        movies_list = [i for i in library if type(i) == Movie]
        sorted_movies = sorted(movies_list, key=lambda item: item.title)
    return sorted_movies

def get_series():
    for i in library:
        series_list = [i for i in library if type(i) == Series]
        sorted_movies = sorted(series_list, key=lambda item: item.title)
    return sorted_movies

# Search by title

def search(find_title):
    for name in library:
        if name.title == find_title:
            return name

# Generate vievs from play definition 

def generate_views(movies_list):
    for _ in range(10):
        for x in movies_list:
            Movie.play(x)
        return movies_list

# Returinng top title 

def top_tittle(top):
    sorted_library = sorted(library, key = attrgetter('number_of_watching'), reverse = True)
    return sorted_library[0:top]



if __name__ == "__main__":
    library=[]
    movies_list =[]
    series_list = []

    print("\nAll movies data\n")

    print(movies_data())

    print("\nMovies sorted list\n")

    print(get_movies())

    print("\nSeries sorted lists\n")

    print(get_series())

    print("\nFind by title\n" )

    print(search("Carlos"))

    print("\nGenerate views \n")

    print(generate_views(library))

    print("\nTop 3\n" )

    print(top_tittle(3))

