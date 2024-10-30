from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import inquirer

# User Input for selecting genre or Top 100
question = [
    inquirer.List('genre',
        message="What genre of film you are looking for?",
        choices=['Horror', "Comedy", "Drama", "Romance", "Animation", "None - Let me see Top 100"],
    ),
]
answers = inquirer.prompt(question)
print(answers['genre'])
if answers['genre'] == 'None - Let me see Top 100':
    url = "https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/"
else:
    url = "https://letterboxd.com/dave/list/official-top-250-narrative-feature-films/genre/" + answers['genre'].lower() + "/"
# print(requests.get(url)) # to see Response code, want Response 200


options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
browser = webdriver.Chrome(options=options) 
browser.get(url)


# get top films from letterboxd through <ul> 
soup = BeautifulSoup(browser.page_source, 'html.parser')
soup.prettify()
data = soup.find('ul', class_="js-list-entries poster-list -p125 -grid film-list")
movie_titles = data.find_all('span', class_="frame-title")
titles = [title.text.strip() for title in movie_titles]
data_rows = data.find_all('li')


# loop through all <li> for each film's info 
for row in data_rows:
    movie_rank = row.find('p', class_="list-number").text
    movie_title = row.find('img')['alt']
    movie_url = "https://letterboxd.com/film/" + row.find('div')['data-film-slug'] + "/"
    print(movie_rank, movie_title, movie_url)