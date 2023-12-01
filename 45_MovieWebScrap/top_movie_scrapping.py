from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
res = requests.get(URL)
web_html = res.text

soup = BeautifulSoup(web_html, 'html.parser')
title_tags = soup.find_all(
    name='h3', class_="listicleItem_listicle-item__title__hW_Kn")
movies = [t.getText() for t in title_tags]
movies.reverse()

with open('movies.txt', 'w') as m_file:
    for m in movies:
        m_file.write(m + '\n')
