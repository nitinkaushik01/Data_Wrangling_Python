
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

Route_Data_1 = pd.read_csv('Route_Data_1.csv')
Route_Data_1


# In[3]:

Route_Data_2 = pd.read_csv('Route_Data_2.csv')
Route_Data_2


# In[5]:

Bus_Code_Data = pd.read_csv('Bus_Code_Data.csv')
Bus_Code_Data


# In[6]:

#Full Outer Join
pd.merge(Route_Data_1, Route_Data_2, on='Route_ID', how='outer')


# In[7]:

#Right outer join
pd.merge(Route_Data_1, Route_Data_2, on='Route_ID', how='right')


# In[8]:

#Left outer join
pd.merge(Route_Data_1, Route_Data_2, on='Route_ID', how='left')


# In[9]:

#inner join
pd.merge(Route_Data_1, Route_Data_2, on='Route_ID', how='inner')


# In[10]:

#Suffixing column names
pd.merge(Route_Data_1, Route_Data_2, on='Route_ID', how='right' , suffixes=('_leftdf', '_rightdf'))


# In[11]:

#Join on the basis of indexe
pd.merge(Route_Data_1, Route_Data_2, right_index=True, left_index=True)


# In[12]:

pd.concat([Route_Data_1, Route_Data_2], axis=1)


# In[15]:

#Join along rows
df = pd.concat([Route_Data_1, Route_Data_2])
df


# In[16]:

pd.merge(df, Bus_Code_Data, on='Route_ID')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



