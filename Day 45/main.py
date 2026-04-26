import requests
from bs4 import BeautifulSoup
import json

movies_url = "https://editorial.rottentomatoes.com/guide/best-movies-21st-century/"
response = requests.get(movies_url)

soup = BeautifulSoup(response.content, "html.parser")


# number = [indicator.get_text() for indicator in soup.find_all("span", {"class": "indicator"})]
# title = [title.get_text() for title in soup.find_all("a", {"class": "meta-title"})]

movie_block = soup.find_all("div", {"class": "block-countdown rkv-block"})

# with open("top100.txt", "a") as file:
#     for movie in movie_block:
#         indicator = movie.find("span", {"class": "indicator"})
#         title = movie.find("a", {"class": "meta-title"})
#         indicator = indicator.get_text()
#         title = title.get_text()
#
#         file.write(f"{indicator} {title}\n")



movies_list = []

with open('movies.json', 'w') as outfile:
    for movie in movie_block:
        indicator = movie.find("span", {"class": "indicator"})
        title = movie.find("a", {"class": "meta-title"})
        indicator = indicator.get_text()
        title = title.get_text()
        movies_list.append({"rank": indicator, "title": title})

    json.dump(movies_list, outfile, indent=4, ensure_ascii=False)
