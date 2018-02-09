# Homework 13 - Web Scraping

# Sites to Scrape:
# 1) NASA Mars News Site: https://mars.nasa.gov/news/
# 2) PL Mars Space Images - Featured Image: https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
# 3) Mars Weather (Twitter): https://twitter.com/marswxreport?lang=en
# 4) Mars Facts: https://space-facts.com/mars/
# 5) Mars Hemispheres: https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars


# Import Dependencies
import time
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver

def init_browser():
    executable_path = {"executable_path": "C:/Users/chris/Desktop/UCI Apps/chromedriver"}
    return Browser("chrome", **executable_path, headless=True)


# Create a single function called `scrape` that will execute all
# of the scraping code and return one Python dictionary containing
# all of the scraped data.

def scrape():
    browser = init_browser()

    # 1) NASA Mars News Site: https://mars.nasa.gov/news/
    # -----------------------------------------------------------------------------------------------------------
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    time.sleep(1)
    
    news_html = browser.html
    news_soup = BeautifulSoup(news_html, "html.parser")

    title = news_soup.find("div", class_="content_title").get_text()
    par = news_soup.find("div", class_="article_teaser_body").get_text()
    
    news_dict = {"news_title": title,
                "news_par": par}
    
    # -----------------------------------------------------------------------------------------------------------

    # 2) PL Mars Space Images - Featured Image: https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
    # -----------------------------------------------------------------------------------------------------------
    img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(img_url)
    time.sleep(1)

    browser.click_link_by_partial_text("FULL IMAGE")
    time.sleep(5)
    browser.click_link_by_partial_text("more info")

    img_html = browser.html
    img_soup = BeautifulSoup(img_html, "html.parser")

    partial_url = img_soup.find("figure").find("img")["src"]
    
    featured_img_url = str("https://www.jpl.nasa.gov" + partial_url)
    featured_img_dict = {"featured_image": featured_img_url}
    
    # -----------------------------------------------------------------------------------------------------------

    # 3) Mars Weather (Twitter): https://twitter.com/marswxreport?lang=en
    # -----------------------------------------------------------------------------------------------------------
    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)
    time.sleep(1)

    weather_html = browser.html
    twitter_soup = BeautifulSoup(weather_html, "html.parser")
    
    weather = twitter_soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").get_text()    
    weather_dict = {"weather": weather}
    
    # -----------------------------------------------------------------------------------------------------------

    # 4) Mars Facts: https://space-facts.com/mars/
    # -----------------------------------------------------------------------------------------------------------
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)
    time.sleep(1)

    facts_html = browser.html
    facts_soup = BeautifulSoup(facts_html, "html.parser")
    
    #Find all table headers (a.k.a. column 1):
    col1 = facts_soup.find_all("td", class_="column-1")

    tbl_headers = []
    for i in range(0, len(col1)-1):
        text = col1[i].get_text()
        tbl_headers.append(text)
    
    #Find all table data (a.k.a. column 2):
    col2 = facts_soup.find_all("td", class_="column-2")

    tbl_data = []
    for i in range(0, len(col2)-1):
        text = col1[i].get_text()
        tbl_data.append(text)

    #Merge lists into a to pandas dataframe
    df = pd.DataFrame({"Fact": tbl_headers,
                       "Value": tbl_data})
    
    #Convert dataframe to HTML table; align text to the left
    facts = df.to_html().replace('<tr style="text-align: right;">','<tr style="text-align: left;">')
    facts_dict = {"facts_table":facts}
    
    # -----------------------------------------------------------------------------------------------------------

    # 5) Mars Hemispheres: https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
    # -----------------------------------------------------------------------------------------------------------
    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemi_url)
    time.sleep(1)

    html1 = browser.html
    
    #Find names of hemispheres and put them in a list
    hemi_soup = BeautifulSoup(html1, "html.parser")
    headers = hemi_soup.find_all("h3")

    hemisphere_image_urls = []

    for i in range(0, (len(headers))):        
        #Get hemisphere names
        hemi = str(headers[i]).split("<h3>")[1]
        name = hemi[:(len(hemi)-14)]
        
        #Use hemisphere name to click on link and get image URL
        browser.click_link_by_partial_text(name)
        time.sleep(2)
        img_soup = BeautifulSoup(browser.html, "html.parser")
        hemi_url = img_soup.find("div", class_="downloads").find("a")["href"]
        
        #Add the hemisphere name and img url to a dictionary
        temp_dict = {"title": name, "img_url": hemi_url}
        
        #Append the temp_dict to the list
        hemisphere_image_urls.append(temp_dict)
                
        #tell the browser to hit the back button so it can get the next image URL
        browser.back()
        time.sleep(2)
    
    browser.quit()
    # -----------------------------------------------------------------------------------------------------------

    mars_dict = {"mars_news": news_dict,
                "mars_image": featured_img_dict,
                "mars_weather": weather_dict,
                "mars_facts": facts_dict,
                "mars_hemispheres": hemisphere_image_urls
                }

    return mars_dict