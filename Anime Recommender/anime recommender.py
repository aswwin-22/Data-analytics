#!/usr/bin/env python
# coding: utf-8

# # <p style="padding:10px;background-color:#0f4c5c;margin:0;color:white;font-family:newtimeroman;font-size:150%;text-align:center;border-radius: 15px 50px;overflow:hidden;font-weight:500">Anime Ratings Analysis & Recommender System</p>
# 
# <p style="text-align:center; ">
# <img src="https://wallpapercave.com/wp/wp9944149.jpg" style='width: 600px; height: 300px;'>
# </p>
# 
# 
# <p style="text-align:justify; ">
#     
# Every streaming content has its own viewers and each content has it's rating. Viewers leave some good ratings for the content if they like it. But where does it apply? Viewers can spend hours scrolling through hundreds, sometimes thousands of anime's but never getting a content they like. Businesses need to provide suggestions based on viewers likings and needs in order to create a better streaming environment that boosts revenue and increases the time spent on a website.
# </p> 
# 
# <a id='top'></a>
# <div class="list-group" id="list-tab" role="tablist">
# <p style="padding:10px;background-color:purple;margin:0;color:black;font-family:newtimeroman;font-size:230%;text-align:center;border-radius: 15px 50px;overflow:hidden;font-weight:500">Table Of Contents</p>   
#     
# 
#     
# |No  | Contents |No  | Contents  |
# |:---| :---     |:---| :----     |
# |1   | [<font color="#0f4c5c"> Importing Libraries</font>](#1)                   |9   | [<font color="#0f4c5c"> Overall Anime Ratings</font>](#9)   |     
# |2   | [<font color="#0f4c5c"> About Dataset</font>](#2)                         |10  | [<font color="#0f4c5c"> Top Animes Based On Ratings</font>](#10)|      
# |3   | [<font color="#0f4c5c"> Basic Exploration</font>](#3)                     |11  | [<font color="#0f4c5c"> Category-wise Anime Ratings Distribution</font>](#11)   |    
# |4   | [<font color="#0f4c5c"> Dataset Summary</font>](#4)                       |12  | [<font color="#0f4c5c"> Anime Genres</font>](#12)    |       
# |5   | [<font color="#0f4c5c"> Digging Deeper</font>](#5)      |13  | [<font color="#0f4c5c"> Final Data Preprocessing</font>](#13)  |     
# |6   | [<font color="#0f4c5c"> Custom Palette For Visualization</font>](#6)              |14  | [<font color="#0f4c5c"> Collaborative Recommender</font>](#14)     |     
# |7   | [<font color="#0f4c5c"> Top Anime Community</font>](#7)      |15  | [<font color="#0f4c5c"> Content Based Recommender</font>](#15)  |     
# |8   | [<font color="#0f4c5c"> Anime Category</font>](#8)              |16  | [<font color="#0f4c5c"> Thank You</font>](#16)     |     
#    
# 

# <a id="1"></a>
# <div style="padding:10px;background-color:purple;margin:0;color:black;
#             font-family:newtimeroman;font-size:230%;text-align:center;border-radius: 15px 50px;overflow:hidden;font-weight:500">
#     Importing Libraries
# </div>
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# <a id="1"></a>
# <div style="padding:10px;background-color:purple;margin:0;color:black;
#             font-family:newtimeroman;font-size:230%;text-align:center;border-radius: 15px 50px;overflow:hidden;font-weight:500">
#    Reading the dataset
# </div>

# In[5]:


animes = pd.read_csv(r"Downloads/anime.csv")
ratings = pd.read_csv(r"Downloads/rating.csv/rating.csv")


# In[3]:


animes.head().style.set_properties(**{"background-color": "#ff6347","color":"white","border": "1.5px  solid black"})


# In[4]:


ratings.head().style.set_properties(**{"background-color": "#3498db","color":"white","border": "1.5px  solid black"})


# <a id="1"></a>
# <div style="padding:10px;background-color:purple;margin:0;color:black;
#             font-family:newtimeroman;font-size:230%;text-align:center;border-radius: 15px 50px;overflow:hidden;font-weight:500">
#    Basic exploration of the data
# </div>

# In[16]:


print("No of rows in animes dataset : ",animes.shape[0])
print("No of columns in animes dataset : ",animes.shape[1])


# In[12]:


print("No of rows in ratings dataset : ",ratings.shape[0])
print("No of columns in ratings dataset : ",ratings.shape[1])


# In[13]:


animes.info()


# In[14]:


ratings.info()


# In[15]:


animes.isna().sum()


# ## Dropping the null values and duplicate values

# In[16]:


animes.dropna(axis=0,inplace=True)


# In[17]:


animes.isna().sum()


# In[18]:


animes.duplicated().sum()


# In[19]:


ratings.isna().sum()


# In[20]:


ratings.duplicated().sum()


# In[21]:


ratings.drop_duplicates(keep='first',inplace=True)


# <a id="1"></a>
# <div style="padding:10px;background-color:purple;margin:0;color:black;
#             font-family:newtimeroman;font-size:230%;text-align:center;border-radius: 15px 50px;overflow:hidden;font-weight:500">
#    Analyzing further
# </div>

# In[22]:


top_20_anime_comm = animes.sort_values('members',ascending=False).head(20)


# In[23]:


colors = plt.cm.viridis(np.linspace(0,1,len(top_20_anime_comm)))

plt.bar(x=top_20_anime_comm['name'], height=top_20_anime_comm['members'],color=colors)
plt.xlabel('Anime Name')
plt.ylabel('Number of Members')
plt.title('Top 20 Anime by Number of Members')
plt.xticks(rotation=90)  
plt.show()


# ## Highest Rated Animes

# In[24]:


highest_rated =animes.sort_values('rating',ascending=False).query("`members`>100").head(10)
highest = animes.sort_values('rating',ascending=False).query("`members`>100").head(10).style.set_properties(**{"background-color": "#ff6347","color":"white","border": "1.5px  solid black"})
highest


# In[25]:


plt.bar(x=highest_rated['name'],height=highest_rated['rating'],color=colors)

plt.xlabel("Anime")
plt.ylabel("Rating")
plt.title("Top 10 Rated Animes")

plt.xticks(rotation=90,ha='right')
plt.show()


# In[26]:


animes['type'].value_counts()


# In[36]:


colors = ['#66b3ff', '#99ff99', '#ffcc99', '#ff9999', '#c2c2f0', '#ffb3e6'] 
plt.figure(figsize=(6,6))  
explode = (0.1, 0, 0, 0, 0, 0)

animes['type'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=colors, explode=explode, startangle=90, shadow=True)

plt.title('Distribution of Anime Categories', fontsize=16, fontweight='bold')

plt.legend(animes['type'].value_counts().index, loc='center right',bbox_to_anchor=(1.3, 0.5))


plt.axis('equal')

plt.show()


# In[22]:


from wordcloud import WordCloud

wordcloud = WordCloud(width = 800, height = 250, background_color ="black",colormap = "cividis",
                      max_font_size=100, stopwords =None,repeat= True).generate(animes["genre"].str.cat(sep=", | , | ,"))

print("let's explore how genre's wordcloud looks like\n")
plt.figure(figsize = (20, 8),facecolor = "#ffd100") 
plt.imshow(wordcloud)
plt.axis("off")
plt.margins(x = 0, y = 0)
plt.tight_layout(pad = 0) 
plt.show()


# <a id="1"></a>
# <div style="padding:10px;background-color:purple;margin:0;color:black;
#             font-family:newtimeroman;font-size:230%;text-align:center;border-radius: 15px 50px;overflow:hidden;font-weight:500">
#    Further organizing the data
# </div>

# In[6]:


fulldata = pd.merge(animes,ratings,on="anime_id",suffixes= [None, "_user"])
fulldata = fulldata.rename(columns={"rating_user": "user_rating"})

print(f"Shape of The Merged Dataset : {fulldata.shape}")
print(f"\nGlimpse of The Merged Dataset :")

fulldata.head().style.set_properties(**{"background-color": "#2a9d8f","color":"white","border": "1.5px  solid black"})


# In[7]:


data = fulldata.copy()
data["user_rating"].replace(to_replace = -1 , value = np.nan ,inplace=True)
data = data.dropna(axis = 0)
print("Null values after final pre-processing :")
data.isna().sum().to_frame().T.style.set_properties(**{"background-color": "#2a9d8f","color":"white","border": "1.5px  solid black"})


# In[8]:


selected_users = data["user_id"].value_counts()
data = data[data["user_id"].isin(selected_users[selected_users >= 50].index)]


# In[9]:


data_pivot_temp = data.pivot_table(index="name",columns="user_id",values="user_rating").fillna(0)
data_pivot_temp.head()


# In[10]:


import re
def text_cleaning(text):
    text = re.sub(r'&quot;', '', text)
    text = re.sub(r'.hack//', '', text)
    text = re.sub(r'&#039;', '', text)
    text = re.sub(r'A&#039;s', '', text)
    text = re.sub(r'I&#039;', 'I\'', text)
    text = re.sub(r'&amp;', 'and', text)
    
    return text

data["name"] = data["name"].apply(text_cleaning)


# In[11]:


data_pivot = data.pivot_table(index="name",columns="user_id",values="user_rating").fillna(0)
print("After Cleaning the animes names, let's see how it looks like.")
data_pivot.head()


# <a id="1"></a>
# <div style="padding:10px;background-color:purple;margin:0;color:black;
#             font-family:newtimeroman;font-size:230%;text-align:center;border-radius: 15px 50px;overflow:hidden;font-weight:500">
#    Recommender
# </div>

# In[9]:


from sklearn.feature_extraction.text import TfidfVectorizer

# Define the TF-IDF vectorizer with desired parameters
tfv = TfidfVectorizer(min_df=3, max_features=None, strip_accents="unicode",
                      analyzer="word", token_pattern=r"\w{1,}", ngram_range=(1, 3), stop_words="english")

# Create a copy of the original dataset and drop duplicates
rec_data = fulldata.copy().drop_duplicates(subset="name", keep="first").reset_index(drop=True)

# Split the "genre" column into a list of genres and convert to string
genres = rec_data["genre"].str.split(", | , | ,").astype(str)

# Apply TF-IDF vectorization
tfv_matrix = tfv.fit_transform(genres)

# Display feature names
feature_names = tfv.get_feature_names_out()

# Create a DataFrame with feature names and their corresponding TF-IDF values
tfidf_df = pd.DataFrame(data=tfv_matrix.toarray(), columns=feature_names)

# Display the result
print(tfidf_df)


# In[27]:


from sklearn.metrics.pairwise import sigmoid_kernel

sig = sigmoid_kernel(tfv_matrix, tfv_matrix)      # Computing sigmoid kernel

rec_indices = pd.Series(rec_data.index, index = rec_data["name"]).drop_duplicates()


# Recommendation Function
def give_recommendation(title, sig = sig):
    
    idx = rec_indices[title] # Getting index corresponding to original_title

    sig_score = list(enumerate(sig[idx]))  # Getting pairwsie similarity scores 
    sig_score = sorted(sig_score, key=lambda x: x[1], reverse=True)
    sig_score = sig_score[1:11]
    anime_indices = [i[0] for i in sig_score]
     
    # Top 10 most similar movies
    rec_dic = {"No" : range(1,11), 
               "Anime Name" : animes["name"].iloc[anime_indices].values,
               "Rating" : animes["rating"].iloc[anime_indices].values}
    dataframe = pd.DataFrame(data = rec_dic)
    dataframe.set_index("No", inplace = True)
    
    print(f"Recommendations for {title} viewers :\n")
    
    return dataframe.style.set_properties(**{"background-color": "#2a9d8f","color":"white","border": "1.5px  solid black"})


# In[28]:


give_recommendation("Death Note")


# In[33]:


give_recommendation("Kimi no Na wa.")


# ## Arigato!

# In[ ]:




