#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from urllib.parse import urlencode
from openpyxl import Workbook
from instascrape import *

wb=Workbook()
page=wb.active

#pass a session_id so instagram doesn't prompt for login credentials
session_id = '863216893%3A8hUnFBS0T84cKP%3A26' 

data = pd.read_csv("insta_file_unscraped.csv")

for index, row in data.iterrows():
    brand_post_url = row['brand_post_url']
    brand = row['brand']
    brand_post = Post(brand_post_url)
    brand_post.scrape()
    for comment in brand_post.get_recent_comments():
        comment_text = str(comment).split(':', 3)
        comment_text.remove('<Comment')
        page.append([brand, brand_post_url, comment_text[0], comment_text[1]])

wb.save(filename = 'insta_comments.xlsx')
