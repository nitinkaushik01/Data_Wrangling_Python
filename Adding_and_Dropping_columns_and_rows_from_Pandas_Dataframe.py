
# coding: utf-8

# In[26]:

import pandas as pd


# In[27]:

data = pd.read_csv('data.csv')
data


# In[37]:

data['Data of Purchase'] = ['2018/02/03', '2017/09/11','2016/05/08','2015/06/06','2017/05/05', '2019/01/01']
data


# In[29]:

data.assign(Location = ['NewYork','San Francisco','Dallas','New Jersey','Atlanta','Madison'])


# In[39]:

data = data.drop('Data of Purchase', axis=1)
data


# In[40]:

data


# In[41]:

data[:2]


# In[42]:

data


# In[43]:

data1 = data.drop(data.index[1])


# In[44]:

data


# In[45]:

data1 = data.drop(data.index[[3,5]])
data1


# In[46]:

data


# In[47]:

data2 = data.drop(data.index[-4])
data2


# In[48]:

data


# In[49]:

data3 = data[:-2]
data3


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



