from faker import Faker
import random
from tabulate import tabulate

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
        return f'{self.title, self.publication_year, self.genre, self.number_of_watching}'  
    
    def __repr__(self):
        return 'Movie(title: %s, publication_year: %s, genre: %s, number_of_watching: %r)' % (self.title, self.publication_year, self.genre, self.number_of_watching)

    def movie_publication_year(self):
        return f'{self.title} ({self.publication_year})'

    def isSeries(self):
        hasattr(Movie, 'season_number')
        return False

    def list_movies(self):
        return [f'{self.title}, {self.publication_year},{self.genre}, {self.number_of_watching}']

#Adding Class about series

class Series(Movie):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f'{self.title}  S{self.season_number}E{self.episode_number} {self.number_of_watching}'

    def __repr__(self):
        return 'Movie(title: %s, publication_year: %s, genre: %s, number_of_watching: %r, episode_number: %r, season_number: %r)' % (self.title, self.publication_year, self.genre, self.number_of_watching, self.episode_number, self.season_number)
    
    def play(self, step=1):
       self.number_of_watching += step

    def isSeries(self):
        hasattr(Movie, 'season_number')
        return True

    def list_series(self):
        return [f'{self.title}, {self.publication_year},{self.genre}, {self.number_of_watching}, E{self.episode_number}, S{self.season_number}']

# Create a movies and series lists as movies_data

genre_list = ['comedy', 'familly', 'romace', 'horror']

def create_movies():
    for _ in range(5):
        movies_list.append(
                Movie(
                    title = fake.first_name(), 
                    publication_year = fake.random_int(min=1980, max=2020),
                    genre = random.choice(genre_list),
                    number_of_watching = fake.random_int(0,100),
                )
            )
    return movies_list

def create_series():
    for _ in range(5):
        movies_list.append(
                Series(
                    title = fake.first_name(), 
                    publication_year = fake.random_int(min=1980, max=2020),
                    genre = random.choice(genre_list),
                    season_number = fake.random_int(0,24),
                    episode_number = fake.random_int(0,10),
                    number_of_watching = fake.random_int(0,100),
                )
            )
    return movies_list

def movies_data():
    create_movies()
    create_series()
    return movies_list

# Get movies 

def get_movies(movies_list):
    film_list = []
    for item in movies_list:
        if item.isSeries() == False:
            film_list.append(item)
    sorted_movies = sorted(film_list, key=lambda item: item.title)
    film_list = [i.list_movies() for i in film_list]
    print("\nList of sorted films")
    print(tabulate(film_list))

def get_series(movies_list):
    series_list = []
    for item in movies_list:
        if item.isSeries() == True:
            series_list.append(item)
    sorted_series = sorted(series_list, key=lambda item: item.title)
    series_list = [i.list_series() for i in series_list]
    print("\nList of sorted series")
    print(tabulate(series_list))


# Search by title 

def search(movies_list):
    result = []
    search_title = input('Enter title you are looking for: ')
    for item in movies_list:
        if item.title == search_title:
            result.append(item)

            if item.isSeries() == False:
                search_movie = [i.list_movie() for i in result]
                print(tabulate(search_movie))

            elif item.isSeries() == True:
                search_movie = [i.list_series() for i in result]
                print(tabulate(search_movie))


# Generate vievs from play definition 
def generate_views(movies_list):
    for _ in range(10):
        for x in movies_list:
            Movie.play(x)
        return movies_list

# Showing top title 

def top_titles(list_movies):
    top = int(input("How many top movie do you want to see?: "))
    for item in list_movies:
        watches = (sorted(list_movies, key=lambda item: item.number_of_watching))
    top_watches = watches[0:top]
    top_list = [t.list_movies() for t in top_watches]
    print('Your top titles are: ')
    print(tabulate(top_list))

if __name__ == "__main__":
    movies_list=[]

    movies_data()
    #print(movies_list)

    generate_views(movies_list)

    print("\nMovies and Series library\n")

    get_movies(movies_list)

    get_series(movies_list)

    top_titles(movies_list)

    search(movies_list)