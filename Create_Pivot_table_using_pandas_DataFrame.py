
# coding: utf-8

# In[1]:

import pandas as pd


# In[5]:

Data = {'Region': ['East', 'East', 'East', 'East', 'West', 'West', 'West', 'West', 'South', 'South', 'South', 'South', 'North', 'North', 'North', 'North'], 
        'Product': ['Milk', 'Milk', 'Bread', 'Bread', 'Milk', 'Milk', 'Bread', 'Bread','Milk', 'Milk', 'Bread', 'Bread', 'Milk', 'Milk', 'Bread', 'Bread'], 
        'UnitCost': [9.70, 16.60, 7.50, 9.90, 3.45, 4.40, 8.45, 5.40, 17.90, 12.70, 11.60, 3.56, 8.80, 6.75, 10.10, 5.50]}
df = pd.DataFrame(Data, columns = ['Region', 'Product', 'UnitCost'])
df


# In[6]:

#Create a pivot table to calculate the sum of UnitCost by Region and Product
pd.pivot_table(df, index=['Region','Product'], aggfunc='sum')


# In[7]:

#Create a pivot table to calculate the mean of UnitCost by Region and Product
pd.pivot_table(df, index=['Region','Product'], aggfunc='mean')


# In[8]:

#Create a pivot table to calculate count of UnitCost by Region and Product 
pd.pivot_table(df, index=['Region','Product'], aggfunc='count')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



