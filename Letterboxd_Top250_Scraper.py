from bs4 import BeautifulSoup
from selenium import webdriver
import requests



url = "https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/"
# print(requests.get(url)) # to see Response code, want Response 200

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
browser = webdriver.Chrome(options=options) 
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'html.parser')
soup.prettify()
data = soup.find('ul', class_="js-list-entries poster-list -p125 -grid film-list")
movie_titles = data.find_all('span', class_="frame-title")
titles = [title.text.strip() for title in movie_titles]
#print(titles)
data_rows = data.find_all('li')
# print(data)

for row in data_rows:
    movie_rank = row.find('p', class_="list-number").text
    movie_title = row.find('img')['alt']
    movie_url = "/film/" + row.find('div')['data-film-slug'] + "/"
    print(movie_rank, movie_title, movie_url)

# page = requests.get(url)

# soup = BeautifulSoup(page.text, 'html')
# soup.prettify()
# # print(soup.findAll('ul')[20])
# data = (soup.find('ul', class_="js-list-entries poster-list -p125 -grid film-list"))

# movie_rank = (data.findAll('span', class_="frame-title"))

# #text = [title.text.strip() for title in movie_titles]
# print(movie_rank)