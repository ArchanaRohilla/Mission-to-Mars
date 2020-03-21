#import all dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

#Initialize the browser.Create a data dictionary.End the WebDriver and return the scraped data.
def scrape_all():
    # initialize headless driver for deployment
    browser = Browser("chrome", executable_path= "chromedriver", headless=True)
    news_title, news_paragraph = mars_news(browser)
    
    # run all scraping functions and store results in data dictionary
    data = {
        "news_title": news_title,
        "news_paragraph" : news_paragraph,
        "featured_image" : featured_image(browser),
        "facts": mars_facts(),
        "last_modified" : dt.datetime.now()
    }
    return data

#set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path)

def mars_news(browser):

    #visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    #optinal delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html =  browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    
    # add try/except for error handling
    try:
        slide_elem = news_soup.select_one('ul.item_list li.slide')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find("div", class_='content_title').get_text()
        
        #use the parent element to find the paragraph text
        news_paragraph = slide_elem.find('div', class_='article_teaser_body').get_text()
        
    except AttributeError:
        return None, None
    
    return news_title, news_paragraph

# "### Featured Images"

def featured_image(browser):

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

    try:
        #find the relative image url.This way, when NASA updates its image page, our code will still pull the most recent image.
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")
        
        #use the base url to create an absolute url
        img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
        
    except AttributeError:
        return None
        
    return img_url

def mars_facts():
    # add try/except for error handling
    try:
        #scrape the entire facts table with '.read_html()' function.This table settings may need to be modified,if the website changes it.
        #Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://space-facts.com/mars/')[0]
        
    except BaseException:
        return None   
        
    #assign columns and set index of dataframe
    df.columns=['Description', 'Mars']
    df.set_index('Description', inplace=True)
    # convert DataFrame back into HTML format, add bootstrap      
    return df.to_html()

#end the automated browsing session.
browser.quit()

if __name__ == "__main__":
    # if running as script, print scraped data
    print(scrape_all())
