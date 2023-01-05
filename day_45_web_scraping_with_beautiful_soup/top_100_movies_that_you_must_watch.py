from bs4 import BeautifulSoup
import requests
URL ="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# getting hold of webpage
response = requests.get(URL)
top_100_web_page = response.text

# creating soup
soup = BeautifulSoup(top_100_web_page, "html.parser")


all_movies = soup.find_all(name="h3", class_="title")

# print(titles)
# movies_list = []
# for title in titles:
#     movie_name = title.getText()
#     movies_list.append(movie_name)
#
# print(movies_list)

# with open("movies.txt", "a") as movie_txt:
#     movie_txt.write(str(movies_list))


all_titles = [movie.getText() for movie in all_movies]
all_titles_ordered = all_titles[::-1]
# print(all_titles_ordered)

with open("movies.txt", "w") as file:
    for movie_title in all_titles_ordered:
        file.write(f"{movie_title}\n")


