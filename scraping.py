# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt


def scrape_all():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)

    news_title, news_paragraph = mars_news(browser)

    # create a new dictionary in the data dictionary to hold a list of dictionaries with the URL string and title of each hemisphere image.
    marsdata= {}

    # Stop webdriver and return data
    browser.quit()
    return  marsdata


def mars_news(browser):

    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one("ul.item_list li.slide")
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find("div", class_="content_title").get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find("div", class_="article_teaser_body").get_text()

    except AttributeError:
        return None, None

    return news_title, news_p


def featured_image(browser):
    # Visit URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'

    return img_url

def mars_facts():
    html = browser.html
    soup = soup(html, 'html.parser')
    title = soup.find_all('h3')
    url1= 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/images/full.jpg'
    url2= 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/images/schiaparelli_enhanced-full.jpg'
    url3 = 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/images/syrtis_major_enhanced-full.jpg'
    url4 = 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/images/valles_marineris_enhanced-full.jpg'



    dictonary1= {'img_url': url1, 'title': title[0]}
    dictonary2= {'img_url': url2, 'title': title[1]}
    dictonary3= {'img_url': url3, 'title': title[2]}
    dictonary4= {'img_url': url4, 'title': title[3]}


    marsdata = [dictonary1,dictonary2,dictonary3,dictonary4]

    return  marsdata
if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())





