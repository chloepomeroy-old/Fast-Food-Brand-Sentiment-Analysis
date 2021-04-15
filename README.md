# AC---Twitter-Instagram-Sentiments

twitter_scraper.py (made using tweepy) scrapes all recent replies to users specified in "brand_list_twitter.csv" and extracts the brand handle, user handle, user name, content of the reply tweet, and the date and time the reply was posted, outputing it into "twitter_replies.xlsx".

instagram_scraper.py (made using insta-scrape) sscrapes recent replies to instagram posts specified by url in "brand_list_insta.csv" and extracts the brand handle, post url, user handle, and content of the comment, outputing it into "instagram_replies.csv". Unfortunately instagram is more difficult to scrape as it doesn't technically allow scraping (whereas twitter has it's own API that developers can use), so we are unable to scrape the date and time of the comment using insta-scrape.

sentiment_analysis_model.py (written using nltk) was not written by me and is almost entirely taken from this tutorial: 
https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk. 
It is a machine learning model that uses natural language processing to conduct sentiment analysis. I used the built-in nltk.corpus twitter_samples to train the model, but I also added a number of my own examples from twitter that included emojis, in the hopes of improving the model. At this time the model is still not extremely accurate, but my added samples did make an improvement and further exploration could be done into this to continue to improve the accuracy.

classify.py is just a simple file that reads the data from "twitter_replies.xlsx" and "instagram_replies.xlsx" (which must be specified in the code, by default it is "twitter_replies.xlsx") and applies the sentiment analysis model to the data.
