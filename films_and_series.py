from faker import Faker
import random

print("Biblioteka Filmów:\n")

class Film:
    def __init__(self, title, publication_year, gentre, number_of_watching):
        self.title = title
        self.publication_year = publication_year
        self.gentre = gentre
        
        self.number_of_watching = number_of_watching

    def play(self, step=1):
       self.number_of_watching += step

    def __str__(self):
        return f'{self.title} ({self.publication_year}) {self.number_of_watching}'    

class Series(Film):
    def __init__(self, epizode_number, season_number, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.epizode_number = epizode_number
        self.season_number = season_number

    def __str__(self):
        return f'{self.title}  S{self.season_number}E{self.epizode_number} {self.number_of_watching}'     

def search(movie_title):
    for name in list_of_movies:
        if movie_title == name.title:
            return f'Mamy twój film {name}' 
        else: 
            continue   

def generate_views():
    random_views = random.choice(list_of_movies)
    for _ in range(random.randint(1,100)):
        random_views.play()
    return random_views

list_of_movies = []
films = []
series = []


film1 = Film(title = "Titanic", publication_year = 1995, gentre = "Drama", number_of_watching = 0)
film2 = Film(title = "Mask", publication_year = 1990, gentre = "Comedy", number_of_watching = 0)
film3 = Film(title = "Mask2", publication_year = 1998, gentre = "Comedy", number_of_watching = 0)
series1 = Series(title = "BBT", publication_year = 2010, gentre = "Comedy", epizode_number = "02", season_number = "03", number_of_watching=0)
series2 = Series(title = "Friends", publication_year = 1999, gentre = "Comedy", epizode_number = "04", season_number = "05",number_of_watching=0)
series3 = Series(title = "How i meet your mother", publication_year = 2005, gentre = "Comedy", epizode_number = "20", season_number = "08",number_of_watching=0)

list_of_movies.append(film1)
list_of_movies.append(film2)
list_of_movies.append(film3)
list_of_movies.append(series1)
list_of_movies.append(series2)
list_of_movies.append(series3)


films = [i for i in list_of_movies if type(i) == Film]
get_films = sorted(films, key=lambda Film: Film.title)
series = [a for a in list_of_movies if type(a) == Series]
get_series = sorted(series, key=lambda Film: Film.title)

print('Posortowana alfabetycznie lista filmów:')
print(*get_films)
print('\nPosortowana alfabetycznie lista seriali:')
print(*get_series)

print(search("BBT"))

print(generate_views())

final_library = []

def generate_views_10():
    for _ in range(10):
        next_add = generate_views()
        final_library.append(next_add)
    return final_library

print(generate_views_10())