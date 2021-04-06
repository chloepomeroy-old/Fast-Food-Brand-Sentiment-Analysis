#!/usr/bin/env python
# coding: utf-8

from Sentiment_Analysis_Model import classifier

from nltk.tokenize import word_tokenize
from openpyxl import Workbook
import emoji
import pandas as pd

df = pd.read_excel('twitter_replies_only.xls')

column_names = ['brand', 'brand_post_url', 'user', 'user name', 'reply', 'date', 'time', 'sentiment']
wb=Workbook()
page=wb.active
page.append(column_names) #append the first line in the file with the column names

#For each tweet in our scraped tweets, run the sentiment classifier
for index, row in df.iterrows():
    user_reply = row['Text']
    brand = row['brand']
    brand_post_url = row['brand_post_url']
    user = row['user']
    reply_tokens = remove_noise(word_tokenize(emoji.demojize((user_reply)))) #remove noise, tokenize tweets, and translate emojis to words
    sentiment = [brand, brand_post_url, user, user_reply, classifier.classify(dict([token, True] for token in reply_tokens))]
    page.append(sentiment) #append a line in the file with the tweet and sentiment result    

wb.save(filename = 'twitter_sentiments1.xlsx')
