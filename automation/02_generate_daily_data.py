#!/usr/bin/env python
# coding: utf-8

# # PhonePe Automation Project
# 
# ## Notebook 2: Generate Daily Data
# 
# ### Objective
# Generate 50 realistic PhonePe transactions daily based on the existing dataset.
# 
# ### Input
# Original PhonePe Dataset
# 
# ### Output
# Daily Generated Dataset (50 Rows)

# # Extract Existing Values in a way we can easily generate data randomly

# In[18]:


import pandas as pd
import random
from datetime import datetime
import random
import string


# In[2]:


df = pd.read_excel("../data/raw/phonepe_dataset.xlsx")


# In[3]:


df.head()


# In[4]:


services = df["Service"].dropna().unique().tolist()


# In[5]:


service_types = df["Service Type"].dropna().unique().tolist()


# In[7]:


payment_status = df["Payment_Status"].dropna().unique().tolist()


# In[8]:


amount_min = int(df["Amount"].min())


# In[9]:


amount_max = int(df["Amount"].max())


# In[13]:


reasons = df["Reason"].dropna().unique().tolist()


# In[15]:


print(services)
print(service_types)
print(payment_status)
print(reasons)


# # Generate 50 Transactions

# In[21]:


new_data = []

today = datetime.today().strftime("%d-%m-%Y")

for i in range(50):

    transaction_id = "RCG_" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=13))

    user_id = "PP" + str(random.randint(1000000, 9999999))

    service = random.choice(services)

    service_type = random.choice(service_types)

    amount = round(random.uniform(amount_min, amount_max),2)

    status = random.choices(
        ["Success","Failed"],
        weights=[90,10]
    )[0]

    if status=="Success":
        reason="Success"
    else:
        reason=random.choice([
            "Network Error",
            "Server Error",
            "Insufficient Balance"
        ])

    new_data.append([
        transaction_id,
        amount,
        user_id,
        service,
        service_type,
        status,
        reason,
        today
    ])


# # DataFrame

# In[24]:


daily_df = pd.DataFrame(
    new_data,
    columns=df.columns
)

daily_df.head()


# # Save file

# In[26]:


file_name = f"../data/generated/daily_{today}.csv"

daily_df.to_csv(file_name,index=False)

print("50 Daily Transactions Generated Successfully")


# In[ ]:




