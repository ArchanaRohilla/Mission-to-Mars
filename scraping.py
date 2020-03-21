#import splinter, beautiful soup and pandas
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

#set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path)

#visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

#optinal delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

html =  browser.html
news_soup = BeautifulSoup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')

#scrape the article’s title
slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title

#use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# "### Featured Images"

#visit url
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

#find and click the full image button. An id can only be used one time throughout the entire page.
full_image_elem =  browser.find_by_id('full_image')
full_image_elem.click()


#find the more info button and click that.
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.find_link_by_partial_text('more info')
more_info_elem.click()

#parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')

#find the relative image url.This way, when NASA updates its image page, our code will still pull the most recent image.
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel

#use the base url to create an absolute url
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url

#scrape the entire table with Pandas’ .read_html() function.This table settings may need to be modified,if the website changes it.
df = pd.read_html('https://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df

# convert our DataFrame back into HTML-ready code.
df.to_html()

#end the automated browsing session.
browser.quit()
