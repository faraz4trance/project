#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[6]:


import seaborn as sns


# In[7]:


import pandas as pd


# In[9]:


import matplotlib.pyplot as plt


# In[16]:


#Q1
data=pd.read_csv(r'C:/Users/Trance4ever/Downloads/pubg.csv')
data.head()


# In[27]:


#Q2
print(type(data.columns))


# In[24]:


#Q3
data.describe()


# In[25]:


#Q4
# Average person kills 0.91 ( round of to 1) players

#Q5
# 99 percent of people have less than 35 kills 

#Q6
# 35 is the max kill recorded


# In[28]:


#Q7
data.columns


# In[55]:


data_type = data.dtypes
data_type


# In[ ]:





# In[57]:


#Q8
sns.distplot( data['matchDuration'] );


# In[59]:


#Q9
sns.distplot( data['walkDistance'] );


# In[65]:


#Q11

get_ipython().run_line_magic('matplotlib', 'inline')


# match duration
plt.subplot(2,1,1)
plt.plot(data["matchDuration"])
plt.xlabel("Match Duration")

# walkDistance
plt.subplot(2,1,2)
plt.plot(data["walkDistance"])
plt.xlabel("Walk Distance")


# In[67]:


#Q12


get_ipython().run_line_magic('matplotlib', 'inline')

#matchDuration

plt.subplot(1,2,1)
plt.plot(data["matchDuration"])
plt.xlabel("Match Duration")

# walkDistance
plt.subplot(1,2,2)
plt.plot(data["walkDistance"])
plt.xlabel("Walk Distance")


# In[70]:


#Q13

get_ipython().run_line_magic('matplotlib', 'inline')


# kills vs damage dealt
plt.subplot()
plt.plot(data["kills"])
plt.xlabel("damageDealt")


# In[76]:


#Q4
sns.barplot(data['matchType'],data['killPoints']);


# In[78]:


#Q15
sns.barplot(data['matchType'],data['weaponsAcquired']);


# In[79]:


#Q16


# In[83]:


#Q17
sns.boxplot(x='matchType',y='winPlacePerc', data=data);


# In[85]:


#Q18
sns.boxplot(x='matchType',y='matchDuration', data=data);


# In[88]:


#Q19
sns.boxplot( x='matchDuration',y='matchType',data=data);


# In[92]:


#Q20

data['kills'] = data['headshotKills'] + data['teamKills'] + data['roadKills']
data['kills']


# In[94]:


#Q21
data['winPlacePerc'].round(decimals=2)


# In[ ]:


#Q22
# Dont know how to do it 

