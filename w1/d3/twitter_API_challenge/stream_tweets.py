#!/usr/bin/env python
# coding: utf-8

# In[14]:


import twitter
import os
import json


# **Task:** Load the values of access tokens and keys from environmental variables to python variables

# In[15]:


consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET_KEY")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")


# In[16]:


api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)


# In[17]:


# Checking the type of api object
print(type(api))


# In[18]:


## FOLLOWING FUNCTION WILL COLLECT REAL-TIME TWEETS IN OUR COMPUTER

# data returned will be for any tweet mentioning strings in the list FILTER
FILTER = [':)', ':(']

# Languages to filter tweets by is a list. This will be joined by Twitter
# to return data mentioning tweets only in the english language.
LANGUAGES = ['en']


def main():
    with open('sentiment_analysis_tweets.txt', 'a') as f:
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
        for line in api.GetStreamFilter(track=FILTER, languages=LANGUAGES):
            f.write(json.dumps(line))
            f.write('\n')


# In[13]:


# Execute function
main()


# **Task:** Edit function `main` so it can store tweets anywhere (location specified as parameter). The FILTER and LANGUAGES should be parameters as well. Test it with different values and languages.

# **Task:** Create File `stream_tweets.py` that can be executed from the Terminal

# **Task:** Start storing tweets with either happy smiley (`:)`) or sad smiley (`:(`). We will use this dataset during the NLP section.

# In[ ]:




