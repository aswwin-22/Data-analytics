#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[2]:


df = pd.read_csv(r'Downloads/mov_ds/movie_profit.csv')
df.head()


# In[3]:


df.columns


# In[4]:


df.drop(columns={'Unnamed: 0'},inplace=True)
#dropping unwanted columns


# In[5]:


df.info()


# In[6]:


df.isna().sum()
#to find the null values


# In[7]:


df.dropna(inplace =True)
#to drop the null values


# In[8]:


df.isna().sum().sum()


# In[9]:


df.duplicated().sum()


# In[82]:


df.corr()


# In[83]:


x = df['genre']
y = df['worldwide_gross']

plt.figure(figsize = (8,6))
plt.barh(x,y,color = 'lightcoral')
plt.xlabel('Worldwide collection in Billions')
plt.ylabel('Genre')
plt.title('Worldwide collection by Genre')
plt.grid(axis='x', linestyle='--', alpha=0.6)


# In[11]:


df['profit'] = df['worldwide_gross'] - df['production_budget']
df.head()


# In[12]:


df.nlargest(10,'profit')


# In[13]:


most_profitable = df.nlargest(10,'profit')
most_profitable.set_index('movie',inplace=True)


most_profitable.plot(kind='bar',figsize = (10,6))


# In[73]:


df['release_date'] = pd.to_datetime(df['release_date'])
df['released_year'] = df['release_date'].dt.year

plt.figure(figsize=(10,6))
plt.plot(df['released_year'].value_counts(),marker='.')
plt.xlabel('Years')
plt.ylabel('No of movies released')

#this shows that the number of movies released increased drastically from the 1980's to the 2000's and shows slight increase most of the time after 2000


# In[15]:


df['distributor'].value_counts().nlargest(5)


# In[39]:


df['distributor'].value_counts().nlargest(5).plot(kind='bar',color = 'red')
# this graph shows the major distributors who releases the most number of movies


# In[74]:


plt.hist(df['worldwide_gross'],bins=5)
plt.title('Worldwide gross distribution')
plt.xlabel('Collection in Billions')
plt.ylabel('No of movies')


# In[17]:


df.mpaa_rating.value_counts().plot(kind='bar',color = 'green')


# In[18]:


dist_grp = df.groupby('distributor')


# In[19]:


Universalgrp = dist_grp.get_group('Universal')
Universalgrp['production_budget'].mean()


# In[20]:


df['genre'].value_counts().plot(kind='pie',autopct='%1.f%%')


# In[21]:


genre_grp = df.groupby('genre')
genre_grp['profit'].mean().sort_values(ascending=False)

# we can see that 'Adventure' genre movies generate more mean profit followed by 'Action' genre.


# In[43]:


dist_grp['production_budget'].mean().nlargest(5).sort_values(ascending=False)

# we can see that on average 20th Century Fox studio spends more on the production budget


# In[44]:


dist_grp['profit'].sum().nlargest(5)

#20th Century fox has earned the highest amount of profit money 


# In[24]:


dist_grp['profit'].mean().nlargest(5)

# RKO Radio Pictures get the most average profit followed by Columbia pictures


# In[25]:


dist_grp['profit'].mean().nlargest(5).plot(kind='bar')
plt.xlabel('Distributor')
plt.ylabel('Avg profit in billions')
plt.title('Top Avg Profit Distributors')


# In[76]:


#now let us create a scatterplot to check if there is any relationship between production_budget and gross collection
plt.figure(figsize=(10,6))
plt.scatter(df['production_budget'],df['worldwide_gross'])

# we cannot find any major linear relation between production_budget and worldwide gross. If there is any relation , it is very less.


# In[35]:


rating_grp = df.groupby('mpaa_rating')
rating_grp['worldwide_gross'].sum().sort_values(ascending = False)

#here we are grouping the data on ratings and we can see that PG-13 movies has got the highest worldwide collection


# In[46]:


df.head(10)


# In[62]:


df[['movie','genre','worldwide_gross']].sort_values(by='worldwide_gross',ascending=False).head(10)


# In[65]:


biggest_flops = df.nsmallest(10,'profit')
biggest_flops

#these are the biggest flops according to this dataset


# In[ ]:




