import random
from datetime import datetime

class Media:
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.plays = 0

    def play(self):
        self.plays += 1

class Film(Media):
    def __init__(self, title, release_year, genre):
        super().__init__(title, release_year, genre)

    def __str__(self):
        return f"{self.title} ({self.release_year})"

class Serial(Media):
    def __init__(self, title, release_year, genre, season, episode):
        super().__init__(title, release_year, genre)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02}E{self.episode:02}"

def get_movies(movie_or_serial):
    return sorted([media for media in movie_or_serial if isinstance(media, Film)], key=lambda film: film.title)

def get_series(movie_or_serial):
    return sorted([media for media in movie_or_serial if isinstance(media, Serial)], key=lambda serial: serial.title)


def search(movie_or_serial, title):
    for media in movie_or_serial:
        if media.title.lower() == title.lower():
            return media
    return None


def generate_views(movie_or_serial):
    media = random.choice(movie_or_serial)
    media.plays += random.randint(1, 100)

def generate_views_multiple_times(movie_or_serial, times=10):
    for _ in range(times):
        generate_views(movie_or_serial)


def top_titles(movie_or_serial, n=3, content_type=None):
    if content_type == "movies":
        filtered = get_movies(movie_or_serial)
    elif content_type == "series":
        filtered = get_series(movie_or_serial)
    else:
        filtered = movie_or_serial

    return sorted(filtered, key=lambda media: media.plays, reverse=True)[:n]

if __name__ == "__main__":
    print("Biblioteka filmów.")

    # filmy i seriale
    movie1 = Film("Kiler", 1994, "Crime")
    movie2 = Film("Król", 2020, "Crime")
    series1 = Serial("Klan", 1989, "Drama", 1, 5)
    series2 = Serial("Pan", 2023, "Comedy", 2, 10)

    # Lista filmów i seriali
    movie_or_serial = [movie1, movie2, series1, series2]

    generate_views_multiple_times(movie_or_serial, times=10)

    today = datetime.today().strftime("%d.%m.%Y")

    print(f"Najpopularniejsze filmy i seriale dnia {today}:")
    top_titles_list = top_titles(movie_or_serial, n=3)
    for media in top_titles_list:
        print(f"{media} - liczba odtworzeń: {media.plays}")
