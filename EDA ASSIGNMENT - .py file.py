#!/usr/bin/env python
# coding: utf-8

# In[1]:


#MOVIE DATASET
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# In[2]:


df=pd.read_csv("movies_data.csv")
df.head()#give starting five rows


# Attributes of Dataset
# Name,Year,Duration,Genre,Rating,Votes,Director,Actor 1,Actor 2,Actor 3
# 
# 

# In[3]:


df["Actor"]=df['Actor 1']+','+df['Actor 2']+','+df['Actor 3']#combine actor1,2,3

df.head()  


# In[4]:


df.shape#checking shape we do Data preprocessing


# In[5]:


del df['Actor 1']


# In[6]:


df.head()


# In[7]:


del df['Actor 2']
del df['Actor 3']


# In[8]:


df.head()


# In[9]:


df.columns


# In[10]:


df.dtypes


# In[11]:


df.nunique()#uniques values of dataset


# In[12]:


#unique values in column 
for column in df.columns:
    unique_values=df[column].unique()
    print(f'Unique values in {column}:{unique_values}')


# In[13]:


#dulpicate
df.duplicated().sum()


# if we have duplicate df=df.drop_duplicates()

# In[14]:


df.isnull()#check null values


# In[15]:


df.isnull().sum()


# # Descriptive Analysis
# 1.Univariate Analysis

# In[16]:


plt.figure(figsize=(15, 8))
plt.title("Movies")
sns.countplot(x='Year', data=df)
plt.xticks(rotation=90)
plt.show()


# In[17]:


plt.figure(figsize=(10, 5))
plt.title("Movie ")
sns.histplot(x='Rating', data=df, kde=True)
plt.xticks(rotation=90)
plt.show()


# 2. Bivariate Analysis

# In[18]:


sns.jointplot(x=df['Year'], y=df['Duration'], kind='reg')
plt.show()


# In[19]:


ax = sns.jointplot(x=df['Year'], y=df['Duration'], kind='kde')
plt.show()


# In[20]:


pairs = df[['Name', 'Year', 'Duration', 'Genre']]
sns.pairplot(pairs)
plt.show()


# In[ ]:




