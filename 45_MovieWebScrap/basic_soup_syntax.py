from bs4 import BeautifulSoup

with open('webpage.html', 'r', encoding='utf-8') as h_file:
    contents = h_file.read()

soup = BeautifulSoup(contents, 'html.parser')

# Access html tags using python object syntax
# content of HTML as python object, prettify() indents HTML
print(soup.prettify())
print(soup.title)  # print <title> content of html file
print(soup.title.name)  # give name of tag
print(soup.title.string)  # give value of tag

print(soup.a)  # returns the first anchor tag
print(soup.p)  # returns the first paragraph tag

print(soup.find_all(name='a'))  # returns all anchor tags within HTML in a list
# get all span tags with class score
print(soup.find_all(name='span', class_='score'))
print(soup.find(name="h1", id="name"))  # returns first instance <h1 id="name">
# returns first instance <h3 class="heading">
print(soup.find(name="h3", class_="heading"))

for tag in soup.find_all(name='a'):
    print(tag.string)  # get only content within anchor tag
    print(tag.getText())  # also get content within anchor tag
    print(tag.get('href'))  # get value of href attribute

# returns first instance of anchor tag within paragraph tag <p> <a href="#">
print(soup.select_one(selector='p a'))
print(soup.select_one(selector="#name"))  # returns tag with id="name"

# return list of all elements with .heading class
print(soup.select(selector=".heading"))
