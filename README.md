# Python Web Scraping Projects

### Packages

- <a href="https://pypi.org/project/beautifulsoup4/">Beautiful Soup</a>
- <a href="https://pypi.org/project/selenium/">Selenium</a>
- <a href="https://scrapy.org/">Scrapy</a>
- <a href="https://pypi.org/project/pymongo/">Pymongo</a>
- <a href="https://pypi.org/project/inquirer/">Inquirer</a>

## <a href="https://github.com/AndyEstevez/Python-WebScrape-Projects/blob/main/Letterboxd_Top250_Scraper.py">Get Top 100 and Top Genre-specific films from Letterboxd's Top 250</a>
    - Used BeautifulSoup and Selenium Webdriver to scrape HTML content
    - Used Inquirer for prompting for user input<br>
<img src="images/letterboxd_topfilms.png" height='auto' width='auto'/>



## <a href="https://github.com/AndyEstevez/Python-WebScrape-Projects/tree/main/goodreads_fiction">Get Top 1000 Fiction books from Goodreads community</a>
    - Used Scrapy for getting HTML info and save to json
    - Store into MongoDB with Scrapy pipeline
    - No duplicate items getting stored into MongoDB when running the spider <br>
<img src="images/goodreads_db.png" height='auto' width='auto'/>

## <a href="https://github.com/AndyEstevez/Python-WebScrape-Projects/tree/main/baseballhats">Get all NY Mets hats from MLBShop</a>
    - Used Scrapy for extracting data
    - Saved into MongoDB from pipeline, Output log to file
    - Spider Contracts for assertions in scraping data <br>
<img src="images/scrapy_contracts.png" height='auto' width='auto'/> 