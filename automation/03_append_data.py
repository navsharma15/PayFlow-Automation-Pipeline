#!/usr/bin/env python
# coding: utf-8

# # Okay we already done extract data then generateed data daily 
# # now next step is append generated_dataset into original_dataset 

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


original_df = pd.read_excel("../data/raw/phonepe_dataset.xlsx")


# In[9]:


daily_df = pd.read_csv("../data/generated/daily_19-07-2026.csv")


# In[12]:


daily_df.shape


# In[13]:


original_df.shape


# In[14]:


master_df = pd.concat(
    [original_df, daily_df],
    ignore_index=True
)


# In[15]:


master_df.shape


# In[16]:


master_df.to_csv(
    "../data/processed/master_raw_dataset.csv",
    index=False
)


# In[ ]:




