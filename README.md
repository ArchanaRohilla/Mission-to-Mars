# Mission-to-Mars
Web Scraping to Extract Online Data:
Web scraping is a method used by organizations worldwide to extract online data for analysis. Large companies employ web scraping 
to assess their reputations or track their competitors’ online presence.

## Project Overview 
In this project, a web browser is automated to visit different websites to extract data about the "Mission to Mars". Scraped data was 
stored in a NoSQL database, and then rendered in a web application created with Flask.

In this project, a wed page has been designed using the live scrapped data about 
Mars planet from different NASA/gov websites.The images of four Mars Hemispheres have
also been included in the web page.

## Software
HTML, BeautifulSoup, Splinter, MongoDB, Flask, CSS, Bootstrap 

## Summary of Analysis
A wed page has been designed using the live scrapped data about Mars planet from different NASA/gov websites.
The images of four Mars Hemispheres have also been included in the web page.

### How to run the code:
1.Clone the repository to your local computer, python
2.If you are using Windows, in the scrape_mars.py file, you will need to uncomment lines 9-10 and comment lines 13-14.
3.Open you terminal.
4.'cd' into the directory that holds the repo.
5.Run the command "python scrape_mars.py".
6.Run the command "python app.py".
7.Open your browser and go to "http://localhost:5000/".
8.Click the "Scrap New Data Button" on the web page. It will take about a few moments for the scraping to complete. 
9.Once the scraping function is complete, the updated data will be displayed on the webpage.