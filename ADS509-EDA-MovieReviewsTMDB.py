import pandas as pd
import requests
import json

# import urllib library
from urllib.request import urlopen

import requests
import nltk
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
from wordcloud import WordCloud
import os
#import spacy
#nlp = spacy.load('en_core_web_sm')
#from textblob import TextBlob
#from pattern.en import sentiment

############################################################################
# User Permissions including API key
############################################################################

# API Key
headers = {'Authorization': 'e95058e19672974e3bfe2ba1036729b1'}
apikey = 'e95058e19672974e3bfe2ba1036729b1'

############################################################################
# Perform request to TMDB API
############################################################################
# Get a bunch of movies out of the database
url = 'https://api.themoviedb.org/3/discover/movie?api_key=e95058e19672974e3bfe2ba1036729b1'
response = urlopen(url)
data_json = json.loads(response.read())
movie_list = data_json['results']
total_pages = data_json['total_pages']

movies = []

# go page by page for each movie, get movie id and put into list
for i in range(1,total_pages):
    for m in movie_list:
        id = m['id']
        movies.append(id)


# go through each movie in list and get the reviews, assign to dataframe, one row per review
df_reviews = pd.DataFrame(columns=['movie_id', 'review_id', 'author', 'author_details', 'rating', 'created_at', 'url', 'content'])


for movie in movies:
    url = f"https://api.themoviedb.org/3/movie/{movie}/reviews?page=1&api_key=e95058e19672974e3bfe2ba1036729b1"
    response = urlopen(url)
    data_json = json.loads(response.read())
    reviews = data_json['results']
    total_review_pages = data_json['total_pages']

    for r in reviews:
        review_entry = [movie, r['id'], r['author'], r['author_details'], r['author_details']['rating'], r['created_at'], r['url'], r['content']]
        df_reviews.loc[len(df_reviews.index)] = review_entry

df_reviews.to_csv('df_reviews.csv')


#df_articles.to_csv('df_articles.csv')
############################################################################
# Parse through JSON and store links to dataframe
############################################################################
"""
for obj in obj_list:
    url = obj['webUrl']
    title = obj['webTitle']
    id = obj['id']

    r = requests.get(url)
    r.encoding = 'utf-8'
    html = r.text
    soup = BeautifulSoup(html)
    text = soup.get_text()

    df_articles.loc[len(df_articles.index)] = [id, title, url, text]
    """
############################################################################
# Retrieve and store text from each link
############################################################################


############################################################################
# Retrieve and store text from each link
############################################################################



############################################################################
# Clean Text
############################################################################



############################################################################
# Conduct EDA
############################################################################

# Printing the first 500 characters in html
print(html[:500])

# Creating a BeautifulSoup object from the HTML
soup = BeautifulSoup(html)
# Getting the text out of the soup
text = soup.get_text()

# Creating a BeautifulSoup object from the HTML
soup = BeautifulSoup(html)
# Getting the text out of the soup
text = soup.get_text()

#having a look at the text
print(text[100:1100])

clean_text= text.replace("n", " ")
clean_text= clean_text.replace("/", " ")
clean_text= ''.join([c for c in clean_text if c != "'"])

