
import lxml

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# a_tag = soup.find_all(name="a")
# print(a_tag)
# for tag in a_tag:
#     print(tag.get("href"))
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# company = soup.select_one(selector="p a")
# print(company)


#
# response = requests.get("https://news.ycombinator.com/")
# yc_webpage = response.text
# soup = BeautifulSoup(yc_webpage, "html.parser")
# article_tag = soup.find_all(name="span", class_="titleline")
# article_text = []
# for article in article_tag:
#     article_title = article.getText()
#     article_text.append(article_title)
# # article_link = article_tag.get("href")
# article_score = soup.find_all(name="span", class_="score")
# scores = []
# for score in article_score:
#     article_score = int(score.getText().split()[0])
#     scores.append(article_score)
# highscore = max(scores)
# index = scores.index(highscore)
# best_article = article_text[index+1]
# print(highscore)
# print(index)
# print(best_article)
# print(article_text)
# print(scores)

# use robot.text at the end of link to see what you can scrape
from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
titles = soup.find_all(name="h3", class_="title")
movie_titles = []
for title in titles:
    movie = title.getText()
    movie_titles.append(movie)
movie_titles.reverse()
print(movie_titles)
