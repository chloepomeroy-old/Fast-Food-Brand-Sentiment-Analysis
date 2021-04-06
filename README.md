# AC---Twitter-Instagram-Sentiments

twitter_scraper.py (made using tweepy) scrapes all recent replies to users specified in "brand_list_twitter.csv" and extracts the brand handle, user handle, user name, content of the reply tweet, and the date and time the reply was posted.

instagram_scraper.py (made using insta-scrape) scrapes recent replies to instagram posts specified by url in "brand_list_insta.csv" and extracts the brand handle, post url, user handle, and content of the comment. Unfortunately instagram is more difficult to scrape as it doesn't technically allow scraping (whereas twitter has it's own API that developers can use), so we are unable to scrape the date and time of the comment using insta-scrape.

