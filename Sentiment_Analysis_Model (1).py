#!/usr/bin/env python
# coding: utf-8

# In[16]:


from nltk.corpus import twitter_samples
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import emoji

import re, string


# In[53]:


def remove_noise(text_tokens, stop_words = ()):
    #Function to remove noise
    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens

def make_token_list(reply_list):
    #function to translate emojis within replies/comments
    token_list = []
    for reply in reply_list:
        token_list.append(word_tokenize(emoji.demojize(reply)))
    return token_list
        
def make_cleaned_list(token_list):
    #function to clean the token list
    cleaned_list = []
    for token in token_list:
        cleaned_list.append(remove_noise(token, stop_words))
    return cleaned_list


# In[80]:


stop_words = stopwords.words('english')

positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')
neutral_tweets = twitter_samples.strings('tweets.20150430-223406.json')


# In[81]:


new_neg_list = ['stfu you literally said women belong in the kitchen on women\'s day 😐', 'This ain\'t it. A chicken tender between 2 pieces of bread. It\'s like a hot dog on a hamburger bun. Save yourself the time and $ and go to popeyes lmao', 'It was disgusting not gonna lie. Never again.', 'fuck you', '🤮🤮 TEACH YOUT EMPLOYEES LAW AND RESPECT MASK EXEMPTIONS', '😢', 'decided to ruin my life by discontinuing the hot fudge stuffed cookies. i’m very sad 😡😡😡', 'let me down once again 😭😭😭', 'discontinuing their fudge stuffed cookies ruined my life 🙃', 'Them biscuits looks like the devil themselves 😆😆😆', 'THAT disgraceful "meal" cost $15.. Look at it. Not only did the guy who claimed he\'s a manager at this location tell my mom he\'s not doing anything about it but also told her "for $15 I can buy you another fucking meal". ur managers aren\'t managing shit. Do something', 'fuck you and ur nasty ass cheese curds', 'I just had the worst service ever at the abbot location in anchorage. What’s up with that?', 'still trash.', 'y’all know y’all wrong for putting all that butter on this damn toast', 'your food program is the equivalent of going out to the street, opening up a trash bag and eating out of it.  That’s how shitty your food is.  Carry on.', 'I went the other day and they wouldn’t add gravy to my Blizzard- manager said I’d have to do it myself!!!! How about you give the customers what they want???', '@TimHortons I’ve done that a few times and nothing. I just get contacted to ask how I can be helped and I never hear back. used to be so much better, and straight forward before all this digital mess.', '@Wendys fix your shit! Give your store access to do refunds tru your fucking app and access to change items for there sto…', '@BurgerKing May I suggest something. Stop posting anything regarding on any of your social media sites or advertisements. It’s a friggin (that word is a substitute for a word that’s more deserving) joke and worst one ever on so many levels. Unless you want to shame yourself more', '@kfc the cashier didn’t allow me to scan my rewards and I was not able to get food. Very upset.', '@dgvohwe0 that looks like assss']
for tweet in new_neg_list:
    #adding further examples to the negative list
    negative_tweets.append(tweet)
    
new_pos_list = ['Yumm 😛 I wish I had one right now!', 'Looks so damn good', 'Loved it ❤️🔥', 'Loved reading this. Jan is an amazing lady!', 'Yes please!!!! 😍😍😍', 'ily so much 🥺 your food sends me. Please hook me up bc my love for it is making me broke', 'new rotisserie chicken bites beats ALL other fast food restaurants, hands down. Best choice ever! 👏👏👏👏🤤', 'Cutest biscuits I’ve ever seen!', 'These are ridiculously good', 'you have NO idea how much joy I got when I pulled up to the drive thru and saw it back on the menu!', 'Ouu this looks so yummy!', 'It’s so goooood!', 'Congratulations 🎊🎈🎉 🍾 to Dairy Queen for creating cruelty free options!!! ❤️❤️❤️❤️❤️❤️', 'the kids liked this', 'I like milkshake', 'Your Reno location is the bomb! From burgers to ice cream cakes...', '@dffewa  Looking good 😍😍👏👏 😎', '@BurkerKing 😍😍😍', '@Wendys 🙌🙌🙌🙌🙌🙌', '@kfc I’m all about that life🔥', '@Timhortons I loooooooove it']
for tweet in new_pos_list:
    #adding further examples to the positive list
    positive_tweets.append(tweet)
    
new_neu_list = [' Bring back the Portobello Mushroom Melt!! 😭', 'Does Wendy’s have iced coffee or is that only in the US?', 'If you guys were affiliated with doordash or eatstreet in my area I\'d be a regular, but as it stands your business is the opposite direction of most commerce with little to no scenic value.', 'when am I going to be able to build my own. I’d love for this option to be added to the app 🤞🏽''what age are y\'all hiring in Philadelphia?', 'should i dip my toe into your guys ice cream rn?', 'How do you keep the Blizzards from melting before it’s delivered to the customer?', 'Had this on Wednesday and was not disappointed. Except that they didn’t mix it all the way to the bottom per usual']
for tweet in new_neu_list:
    #adding further examples to the neutral list
    neutral_tweets.append(tweet)


# In[82]:


positive_tweet_tokens = make_token_list(positive_tweets)
negative_tweet_tokens = make_token_list(negative_tweets)
neutral_tweet_tokens = make_token_list(neutral_tweets)


# In[83]:


positive_cleaned_tokens = make_cleaned_list(positive_tweet_tokens)
negative_cleaned_tokens = make_cleaned_list(negative_tweet_tokens)
neutral_cleaned_tokens = make_cleaned_list(neutral_tweet_tokens)


# In[84]:


def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token

all_pos_words = get_all_words(positive_cleaned_tokens)
all_neg_words = get_all_words(negative_cleaned_tokens)
all_neu_words = get_all_words(neutral_cleaned_tokens)


# In[85]:


def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)

positive_tokens_for_model = get_tweets_for_model(positive_cleaned_tokens)
negative_tokens_for_model = get_tweets_for_model(negative_cleaned_tokens)
neutral_tokens_for_model = get_tweets_for_model(neutral_cleaned_tokens)


# In[86]:


import random

positive_dataset = [(tweet_dict, "Positive")
                     for tweet_dict in positive_tokens_for_model]

negative_dataset = [(tweet_dict, "Negative")
                     for tweet_dict in negative_tokens_for_model]

neutral_dataset = [(tweet_dict, "Neutral")
                   for tweet_dict in neutral_tokens_for_model]

dataset = positive_dataset + negative_dataset + neutral_dataset

random.shuffle(dataset)
#Split data for training/testing
train_data = dataset[:7000]
test_data = dataset[7000:]


# In[87]:


from nltk import classify
from nltk import NaiveBayesClassifier
classifier = NaiveBayesClassifier.train(train_data)


# In[ ]:




