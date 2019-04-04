
# coding: utf-8

# ## Import Libraries

# In[3]:

import pandas as pd
import re


# ## Create a Dataframe with raw continuous column string values.

# In[22]:

rawdata = {'data': ['2018-01-01 35 20736.87      Paul',
                    '2017-06-15 67 10567.70      Harry',
                    '2015-07-23 01 3873.90      Noel',
                    '2011-05-12 56 82320.65      John',
                    '2010-03-26 21 28737.01      Sally',
                    '2016-08-19 82 80327.63      Mary',
                    '2018-08-12 90 30467.92     Steve']}
dataf = pd.DataFrame(rawdata, columns = ['data'])
dataf


# ## Extract Employee Name from the row string

# In[23]:

dataf['Emp_Name'] = dataf['data'].str.extract('([A-Z]\w{0,})', expand = True)
dataf['Emp_Name']


# ## Extract Salary from the row string

# In[24]:

dataf['Salary'] = dataf['data'].str.extract('(\d\d\d\d\d.\d\d)', expand = True)
dataf['Salary']


# ## Extract Data of Joining from the row string

# In[25]:

dataf['DOJ'] = dataf['data'].str.extract('(....-..-..)', expand = True)
dataf['DOJ']


# In[27]:

dataf


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



