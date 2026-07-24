#!/usr/bin/env python
# coding: utf-8

# # In this notebook we will clean the master_dataset

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("../data/processed/master_raw_dataset.csv")


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.info()


# In[6]:


df.dtypes


# In[7]:


df.isnull().sum()


# In[8]:


(df.isnull().sum()/len(df))*100


# In[9]:


df[df.duplicated()]


# In[10]:


df.duplicated().sum()


# # data cleaning process

# In[11]:


df.drop_duplicates(inplace=True)


# In[12]:


df.duplicated().sum()


# In[13]:


df[df.duplicated()]


# In[14]:


df.nunique()


# In[15]:


for col in df.columns:
    print(col)
    print(df[col].unique())
    print("-"*40)


# # remove extra spaces

# In[16]:


df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)


# # Standardize Column Names

# In[17]:


df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")


# In[18]:


df.head()


# # Fill Missing Values

# In[19]:


df["service"] = df["service"].fillna("Recharge_Bills")


# In[20]:


df["service_type"] = df["service_type"].fillna(df["service_type"].mode()[0])


# In[21]:


text_columns = ["service", "service_type"]

for col in text_columns:
    df[col] = df[col].str.title()


# In[22]:


df["user_id"] = df["user_id"].fillna("Unknown")


# In[23]:


df["amount"] = df["amount"].fillna(df["amount"].median())


# In[24]:


df["payment_status"] = df["payment_status"].fillna("Unknown")


# In[25]:


df["reason"] = df["reason"].fillna("Unknown")


# In[26]:


df["date"] = pd.to_datetime(df["date"], format="mixed", dayfirst=True)
df["date"] = df["date"].dt.strftime("%d-%m-%Y")


# In[27]:


df.describe()


# In[28]:


Q1 = df["amount"].quantile(0.25)
Q3 = df["amount"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR

df[(df["amount"] < lower) | (df["amount"] > upper)]


# In[29]:


df[df["amount"] < 0]


# In[30]:


df.dtypes


# # convert data type

# In[31]:


df["transaction_id"] = df["transaction_id"].astype("string")
df["user_id"] = df["user_id"].astype("string")
df["service"] = df["service"].astype("category")
df["service_type"] = df["service_type"].astype("category")
df["payment_status"] = df["payment_status"].astype("category")
df["reason"] = df["reason"].astype("category")
df["date"] = pd.to_datetime(df["date"], format="mixed", dayfirst=True)


# In[32]:


df.dtypes


# In[33]:


df.isnull().sum()


# In[34]:


df[df["transaction_id"].isnull()]


# In[35]:


df[df["date"].isnull()]


# In[36]:


df.dropna(subset=["transaction_id", "date"], inplace=True)


# In[37]:


df.isnull().sum()


# In[38]:


df.to_csv("../Data/clean_data/Cleaned.csv", index=False)






