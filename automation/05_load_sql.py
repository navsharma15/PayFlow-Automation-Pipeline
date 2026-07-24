#!/usr/bin/env python
# coding: utf-8

# # Now we have to connect python with sql server then create database then create table then load clean data in that table

# In[2]:





# In[3]:


import pyodbc

print("pyodbc installed")


# In[4]:


import pyodbc
import pandas as pd


# In[5]:


print(pyodbc.drivers())


# In[6]:


conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=master;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

cursor = conn.cursor()

print("Connected Successfully")


# In[7]:


conn.autocommit = True

cursor.execute("""
IF DB_ID('PhonePeDB') IS NULL
CREATE DATABASE PhonePeDB
""")

print("Database Created Successfully")


# In[8]:


conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=PhonePeDB;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

cursor = conn.cursor()

print("Connected to PhonePeDB")


# In[9]:


cursor.execute("""
IF OBJECT_ID('Transactions', 'U') IS NULL
CREATE TABLE Transactions
(
    Transaction_ID VARCHAR(30),
    Amount DECIMAL(10,2),
    User_ID VARCHAR(20),
    Service VARCHAR(50),
    Service_Type VARCHAR(50),
    Payment_Status VARCHAR(20),
    Reason VARCHAR(100),
    Transaction_Date DATE
)
""")

conn.commit()

print("Table Created Successfully")


# In[10]:


import pandas as pd

df = pd.read_csv("../data/clean_data/Cleaned.csv")


# In[11]:


df.columns


# In[12]:


df.dtypes


# In[13]:


df["transaction_id"] = df["transaction_id"].astype("string")
df["user_id"] = df["user_id"].astype("string")
df["service"] = df["service"].astype("category")
df["service_type"] = df["service_type"].astype("category")
df["payment_status"] = df["payment_status"].astype("category")
df["reason"] = df["reason"].astype("category")
df["date"] = pd.to_datetime(df["date"], format="mixed", dayfirst=True)


# In[14]:


df.dtypes


# In[16]:


cursor.fast_executemany = True

data = list(df.itertuples(index=False, name=None))

cursor.executemany("""
INSERT INTO Transactions
(Transaction_ID, Amount, User_ID, Service,
 Service_Type, Payment_Status, Reason, Transaction_Date)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", data)

conn.commit()


# In[ ]:




