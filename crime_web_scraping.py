# Dependencies
#from splinter import Browser
import requests 
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint
from time import sleep
import time 


def scrape():
    
    crime_info = {}

    #NY DAILY NEWS
    daily_news_url = "https://www.nydailynews.com/new-york/nyc-crime/"
    r = requests.get(daily_news_url) 

    daily_news_soup = BeautifulSoup(r.content, 'html5lib')

    # scrape the first title
    daily_news_article = daily_news_soup.find('a', class_="no-u").get_text()
    
    # Grab the first paragraph
    daily_news_para = daily_news_soup.find('p', class_='preview-text spaced spaced-top story-preview spaced-md').get_text()
    
    # scrape the article url
    daily_news_story_url = daily_news_soup.find('a', class_="no-u")['href']

    # NBC New York
    nbc_url = 'https://www.nbcnewyork.com/news/local/'
    r = requests.get(nbc_url)
    nbc_soup = BeautifulSoup(r.content, 'html5lib')

    # Grab the first title
    nbc_article = nbc_soup.find('h3', class_='story-card__title').find('a').get_text()

    # Grab the paragraph
    nbc_paragraph = nbc_soup.find('div', class_='story-card__text').find('div', class_='story-card__excerpt').find('p').get_text()

    nbc_story_url = nbc_soup.find('h3', class_='story-card__title').find('a')['href']
    # nbc_story_url = nbc_story_url.replace('//', 'https://')

    # NY Times
    ny_times_url = 'https://www.nytimes.com/section/nyregion'
    r = requests.get(ny_times_url)
    ny_times_soup = BeautifulSoup(r.content, 'html5lib')

    # Grab the first title
    nytimes_article = ny_times_soup.find('div', class_='css-10wtrbd').find('h2').text

    #Grab the paragraph
    nytimes_paragraph = ny_times_soup.find('div', class_='css-10wtrbd').find('p').text

    #Grab the URL of the article
    nytimes_storyl_route = ny_times_soup.find('div', class_='css-10wtrbd').find('a')['href']
    nytimes_story_url = ny_times_url.replace('/section/nyregion', nytimes_storyl_route)


    # Pix 11 - updated due to Pix11 website redesign - AR
    pix11_url = 'https://pix11.com/category/local-stories/'
    r = requests.get(pix11_url)
    pix11_soup = BeautifulSoup(r.content, 'html5lib')

    # Grab the first title
    pix11_article = pix11_soup.find('h3', class_='ListItem-title').text

    #Grab the url
    pix11_story_url = pix11_soup.find(
        'a', class_='ListItem')['href']

    r = requests.get(pix11_story_url)
    pix11_soup = BeautifulSoup(r.content, 'html5lib')

    pix11_paragraph = pix11_soup.find('div', class_= 'RichTextArticleBody').find('p').get_text()

    # Twitter
    nycem_tweet_url = 'https://twitter.com/NotifyNYC'
    r = requests.get(nycem_tweet_url)
    nycem_tweet_soup = BeautifulSoup(r.content, 'html5lib')

    # Scrape the tweet info
    nycem_tweet = nycem_tweet_soup.find('p', class_='TweetTextSize').text

    #NYPDNEWS
    nypd_tweet_url = 'https://twitter.com/NYPDnews'
    r = requests.get(nypd_tweet_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    nypd_tweet_soup = BeautifulSoup(r.content, 'html5lib')

    # Scrape the tweet info
    nypd_tweet = nypd_tweet_soup.find('p', class_='TweetTextSize').text

    #NYPD SCHOOL SAFETY
    nypd__schools_tweet_url = 'https://twitter.com/NYPDSchools'
    r = requests.get(nypd__schools_tweet_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    nypd_schools_tweet_soup = BeautifulSoup(r.content, 'html5lib')

    # Scrape the tweet info
    nypd_schools_tweet = nypd_schools_tweet_soup.find(
        'p', class_='TweetTextSize').text

    #NYPD Crime Stoppers
    crime_stoppers_url = 'https://twitter.com/NYPDTips'
    r = requests.get(crime_stoppers_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    crime_stoppers_soup = BeautifulSoup(r.content, 'html5lib')

    # Scrape the tweet info
    crime_stoppers_tweet = crime_stoppers_soup.find(
        'p', class_='TweetTextSize').text


    crime_info = {
        'daily_news_article': daily_news_article,
        'daily_news_paragraph': daily_news_para,
        'daily_news_story_url': f'https://www.nydailynews.com{daily_news_story_url}',
        'nbc_article': nbc_article,
        'nbc_paragraph': nbc_paragraph,
        'nbc_story_url': nbc_story_url,
        'nytimes_article': nytimes_article,
        'nytimes_paragraph': nytimes_paragraph,
        'nytimes_story_url': nytimes_story_url,
        'pix11_article': pix11_article,
        'pix11_paragraph': pix11_paragraph,
        'pix11_story_url': pix11_story_url,
        'nycem_tweet_url': nycem_tweet_url,
        'nycem_tweet': nycem_tweet,
        'nypd_tweet_url': nypd_tweet_url,
        'nypd_tweet': nypd_tweet,
        'nypd__schools_tweet_url': nypd__schools_tweet_url,
        'nypd_schools_tweet': nypd_schools_tweet,
        'crime_stoppers_url': crime_stoppers_url,
        'crime_stoppers_tweet': crime_stoppers_tweet,
    }    
    
    return crime_info



