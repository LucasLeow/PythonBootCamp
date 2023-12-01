from bs4 import BeautifulSoup
import requests

res = requests.get('https://news.ycombinator.com/news')
yc_webpage = res.text
soup = BeautifulSoup(yc_webpage, 'html.parser')

article_text = []
article_links = []
article_scores = []

# Get name of all articles
all_anchor_tags = soup.select(selector='a[rel="noreferrer"]')
for a in all_anchor_tags:
    article_text.append(a.string)
    article_links.append(a.get('href'))

all_score_tags = soup.select(selector='.score')
for t in all_score_tags:
    article_scores.append(int(t.string.split(' ')[0]))

max_num_idx = article_scores.index(max(article_scores))
# Idea: Webscrap most popular article and send to email daily
text_format = f"""
Most Popular Article:
Article Title: {article_text[max_num_idx]}
Article Link: {article_links[max_num_idx]}
Article Score: {article_scores[max_num_idx]}
"""

print(text_format)
