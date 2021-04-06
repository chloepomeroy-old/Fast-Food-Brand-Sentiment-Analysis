#!/usr/bin/env python
# coding: utf-8

# In[23]:


from Sentiment_Analysis_Model import classifier


# In[24]:


import pandas as pd

df = pd.read_excel('twitter_replies_only.xls')


# In[25]:


from nltk.tokenize import word_tokenize
from openpyxl import Workbook
import emoji

column_names = ['brand', 'brand_post_url', 'user', 'reply', 'sentiment']
wb=Workbook()
page=wb.active
page.append(column_names) #append the first line in the file with the column names

#For each tweet in our scraped tweets, run the sentiment classifier
for index, row in df.iterrows():
    user_reply = row['Text']
    brand = row['brand']
    brand_post_url = row['brand_post_url']
    user = row['user']
    reply_tokens = remove_noise(word_tokenize(emoji.demojize((user_reply)))) #remove noise and tokenize tweets
    sentiment = [brand, brand_post_url, user, user_reply, classifier.classify(dict([token, True] for token in reply_tokens))]
    page.append(sentiment) #append a line in the file with the tweet and sentiment result    


# In[26]:


wb.save(filename = 'twitter_sentiments1.xlsx')


# In[ ]:




