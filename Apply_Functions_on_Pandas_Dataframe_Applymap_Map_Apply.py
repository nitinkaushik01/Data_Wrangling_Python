
# coding: utf-8

# ## Import Libraries

# In[17]:

#Import os Library for changing the working directory
import os
os.chdir('F:')


# In[20]:

#Import pandas and numpy Libraries
import pandas as pd
import numpy as np


# ## Read the .csv data file

# In[33]:

df = pd.read_csv('iris.csv')
df.head()


# ## Lambda and Apply Function usage

# In[23]:

capitalize = lambda x: x.upper()
df['Species'].apply(capitalize)


# In[25]:

df['Species']


# ## Lambda and Map function usage

# In[26]:

df['Species'].map(capitalize)


# In[28]:

#Dropping unwanted columns
df = df.drop(['Id','Species'], axis=1)
df.head()


# ## ApplyMap function usage on Built-In function (sqrt, square)

# In[31]:

df.applymap(np.sqrt)


# In[32]:

df.applymap(np.square)


# ## ApplyMap function usage on User Defined Functions

# In[35]:

def multiply50(x):
    if type(x) is str:
        return x
    else:
        return 50*x


# In[36]:

df.applymap(multiply50)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



