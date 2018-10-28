#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[2]:


df = sns.load_dataset('titanic')


# In[3]:


df.head()


# In[4]:


df.to_csv('../../data/processed/titanic.csv', index=False)


# In[ ]:




