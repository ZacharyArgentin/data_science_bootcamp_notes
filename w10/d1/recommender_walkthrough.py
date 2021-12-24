#!/usr/bin/env python
# coding: utf-8

# # Recommender system tutorial

# In[2]:

print("running script")
import pandas as pd


# In[3]:


metadata = pd.read_csv("/Users/zacharyargentin/Programming/datasets/movies_dataset/movies_metadata.csv", low_memory=False)
metadata.head(3)


# # Simple Recommender

# wr = (vR / (v + m)) + mC / (v + m).  
# 
# v = vote_count     
# R = vote_average   
# C = mean rating across all movies   
# m = minimum vote count to be considered   
# 

# In[4]:


C = metadata["vote_average"].mean()
C


# In[5]:


m = metadata["vote_count"].quantile(0.90)
m


# In[6]:


q_movies = metadata.copy().loc[metadata["vote_count"].ge(m)]
q_movies.shape


# In[7]:


# Function that computes the weighted rating of each movie
# wr = (vR / (v + m)) + mC / (v + m).
def weighted_rating(x, m=m, C=C):
    v = x["vote_count"]
    R = x["vote_average"]
    return (v/(v+m) * R) + (m/(m+v) * C)


# In[8]:


q_movies["score"] = q_movies.apply(weighted_rating, axis=1)


# In[9]:


#Sort movies based on score calculated above
q_movies = q_movies.sort_values('score', ascending=False)

#Print the top 15 movies
q_movies[['title', 'vote_count', 'vote_average', 'score']].head(20)


# # Content-Based Recommender

# In[10]:


metadata["overview"].head()


# In[11]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[12]:


tfidf = TfidfVectorizer(stop_words="english")
metadata["overview"] = metadata["overview"].fillna("")
tfidf_matrix = tfidf.fit_transform(metadata["overview"])


# In[13]:


tfidf_matrix.shape


# In[14]:


tfidf.get_feature_names()[5000:5010]


# With this matrix in hand, you can now compute a similarity score. There are several similarity metrics that you can use for this, such as the manhattan, euclidean, the Pearson, and the cosine similarity scores.
# 
# since you have used the TF-IDF vectorizer, calculating the dot product between each vector will directly give you the cosine similarity score. Therefore, you will use sklearn's linear_kernel() instead of cosine_similarities() since it is faster.

# In[15]:


from sklearn.metrics.pairwise import linear_kernel
# from sklearn.metrics.pairwise import cosine_similarity


# In[16]:


cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)


# In[17]:


cosine_sim.shape


# In[18]:


cosine_sim[351]


# In[19]:


#Construct a reverse map of indices and movie titles
indices = pd.Series(metadata.index, index=metadata["title"]).drop_duplicates()
indices.head()


# In[20]:


indices[:10]


# #### get recommendation function explained

# In[21]:


indices["Forrest Gump"]


# In[22]:


list(enumerate(cosine_sim[351]))


# In[23]:


sorted(list(enumerate(cosine_sim[351])), key=lambda x: x[1], reverse=True)


# In[24]:


sorted(list(enumerate(cosine_sim[351])), key=lambda x: x[1], reverse=True)[1:11]


# In[25]:


[i[0] for i in sorted(list(enumerate(cosine_sim[351])), key=lambda x: x[1], reverse=True)[1:11]]


# In[26]:


metadata['title'].iloc[[i[0] for i in sorted(list(enumerate(cosine_sim[351])), key=lambda x: x[1], reverse=True)[1:11]]]


# In[27]:


def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    titles = metadata["title"].iloc[movie_indices]
    return titles


# In[28]:


get_recommendations("Toy Story")


# > The recommendations aren't very good using only the plot.   
# > let's add more features

# In[29]:


credits = pd.read_csv("/Users/zacharyargentin/Programming/datasets/movies_dataset/credits.csv")
keywords = pd.read_csv("/Users/zacharyargentin/Programming/datasets/movies_dataset/keywords.csv")


# In[30]:


# Remove rows with bad IDs.
metadata = metadata.drop([19730, 29503, 35587])


# In[31]:


metadata.head(3)


# In[32]:


credits.head(3)


# In[33]:


keywords.head(3)


# In[34]:


# Convert IDs to int. Required for merging
keywords['id'] = keywords['id'].astype('int')
credits['id'] = credits['id'].astype('int')
metadata['id'] = metadata['id'].astype('int')


# In[35]:


# Merge keywords and credits into your main metadata dataframe
metadata = metadata.merge(credits, on="id")
metadata = metadata.merge(keywords, on="id")


# In[36]:


metadata.head(3)


# In[37]:


# Parse the stringified features into their corresponding python objects
from ast import literal_eval

features = ['cast', 'crew', 'keywords', 'genres']
for feature in features:
    metadata[feature] = metadata[feature].apply(literal_eval)


# In[38]:


metadata.head(2)


# In[39]:


metadata["crew"][0][0]


# In[40]:


import numpy as np


# In[41]:


def get_director(x):
    for i in x:
        if i["job"] == ("Director"):
            return i["name"]
    return np.nan


# In[42]:


def get_list(x):
    if isinstance(x, list):
        names = [i["name"] for i in x]
        if len(names) > 3:
            return names[:3]
        return names
    return[]


# In[43]:


metadata["director"] = metadata["crew"].apply(get_director)


# In[44]:


features = ['cast', 'keywords', 'genres']
for feature in features:
    metadata[feature] = metadata[feature].apply(get_list)


# In[45]:


metadata[["title", "cast", "genres", "keywords", "director"]].head(3)


# In[46]:


# Function to convert all strings to lower case and strip names of spaces
def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        #Check if director exists. If not, return empty string
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''


# In[47]:


# Apply clean_data function to your features.
features = ['cast', 'keywords', 'director', 'genres']

for feature in features:
    metadata[feature] = metadata[feature].apply(clean_data)


# In[48]:


def create_soup(x):
    return ' '.join(x['keywords']) + ' ' + ' '.join(x['cast']) + ' ' + x['director'] + ' ' + ' '.join(x['genres'])


# In[49]:


metadata['soup'] = metadata.apply(create_soup, axis=1)


# In[50]:


metadata[['soup']].head(2)


# In[51]:


from sklearn.feature_extraction.text import CountVectorizer


# In[52]:


count = CountVectorizer(stop_words="english")
count_matrix = count.fit_transform(metadata["soup"])


# In[53]:


count_matrix.shape


# In[54]:


from sklearn.metrics.pairwise import cosine_similarity


# ### kernal dies here for some reason

# In[ ]:


cosine_sim2 = cosine_similarity(count_matrix, count_matrix)


# In[ ]:


# Reset index of your main DataFrame and construct reverse mapping as before
metadata = metadata.reset_index()
indices = pd.Series(metadata.index, index=metadata['title'])


# In[ ]:


get_recommendations('The Dark Knight Rises', cosine_sim2)


# In[ ]:


get_recommendations('The Godfather', cosine_sim2)

