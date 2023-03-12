#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import necessary libs
import pandas as pd
from datetime import datetime


# In[2]:


#import the dataset 
dataset = pd.read_csv(r'C:\Users\agozi\Desktop\internship\CUSTOMER DEMOGRAPHIC.CSV')
print(dataset)


# In[3]:


# convert to dataframe
df = pd.DataFrame (dataset)
df[:2]


# In[4]:


#check for null value
df.isnull().sum()


# In[5]:


# drop null values in DOB since thats the only column needed with null values
df = df.dropna(subset=['DOB'])


# In[7]:


# create age column and group according to age bracket
from datetime import datetime
# convert DOB column to datetime format
df['DOB'] = pd.to_datetime(df['DOB'])

# calculate age based on DOB column
def calculate_age(dob):
    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

df['Age'] = df['DOB'].apply(lambda x: calculate_age(x))
df[:2]


# In[6]:


# create a new column with age groups based on 10-year intervals

df['Age Group'] = df['Age'].apply(lambda x: f'{(x//10)*10}-{((x//10)*10)+9}')

# print the updated DataFrame
df[:2]


# In[ ]:


# export the DataFrame as a CSV file
df.to_csv('C:/Users/agozi/Desktop/internship/customer_demographic_clean.csv', index=False)


# In[ ]:




