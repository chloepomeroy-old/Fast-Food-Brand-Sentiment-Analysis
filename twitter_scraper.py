#!/usr/bin/env python
# coding: utf-8

import csv
import tweepy
import ssl
import pandas as pd
import emoji
from openpyxl import Workbook

ssl._create_default_https_context = ssl._create_unverified_context

# Oauth keys from the Twitter Developer Account
consumer_key = "sOgqlyWHjEI0tyInmHwC9eYFs"
consumer_secret = "vam1WAABMVrqqiThegH1V6X4Ia1JTGGSWwxD2ObULtRu1ZB8x9"
access_token = "2222400198-dJpEiRXKucvOHvEvmEoAmDRiXuMZIr67WRrbkQi"
access_token_secret = "ds7Ofly27GmGOZP0IKXpxciz9YaAfxx8LzTcm95iDKvho"

# Authentication with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = api = tweepy.API(auth, wait_on_rate_limit=True) #wait_on_rate_limit lets us avoid errors due to the twitter APIs rate limits

brand_list = pd.read_csv("brand_list_twitter.csv") #read the list of brands from a file

column_names = ['brand', 'brand_post_url', 'user', 'user name', 'text', 'date', 'time']

wb=Workbook()
page=wb.active
page.append(column_names) #append the first row of the file with the column names

for brand in brand_list['brand']:
    for tweet in tweepy.Cursor(api.search,q='to:'+brand, tweet_mode='extended', timeout=999999).items(300): #Search for tweets to the brand
        if hasattr(tweet, 'in_reply_to_status_id_str'): 
            #Verify that the tweet is a reply
            reply = [brand, 'n/a', tweet.user.screen_name, tweet.user.name, tweet.full_text.replace('\n', ' '), str(tweet.created_at.date()), str(tweet.created_at.time())]
            page.append(reply) #append the file with the reply text

#save the file
wb.save(filename = 'twitter_replies.xlsx')
