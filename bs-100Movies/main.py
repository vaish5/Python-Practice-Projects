import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# Write your code below this line 👇

response = requests.get(URL)
The_100_best_movies_page = response.text

soup = BeautifulSoup(The_100_best_movies_page, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.get_text() for movie in all_movies]
movie_titles_list = movie_titles[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movie_titles_list:
        file.write(f"{movie}\n")
