#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


#create dataframe 1

df0 = pd.DataFrame({"employee":['jos','steven','fap','morris'],
       'group':['rajasthan','rajasthan','chennai','bangalore']})


# In[3]:


#create dataframe 1

df1 = pd.DataFrame({"employee":['jos','steven','fap','morris'],
       'year':[2012,2015,2013,2016]})


# In[4]:


#merge 2 dataset using merge function

df2 = pd.merge(df0,df1)
df2


# In[5]:


#many to 1 join

df3 = pd.DataFrame({'supervisor': ['warne','dharan','kumble'],
                   'group':['rajasthan','chennai','bangalore']})

df4 = pd.merge(df2,df3)
df4


# In[6]:


#many to many join

df5 = pd.DataFrame({'group':['rajasthan','chennai','chennai','bangalore'],
                   'skills':['bowling','batting','bowling','batting']})

df6 = pd.merge(df4,df5)
df6


# In[7]:


#join using on keyword

df7 = pd.merge(df4, df5, on='group')
df7


# In[8]:


df8 = pd.DataFrame({"name":['jos','steven','fap','morris'],
                   'salary':[20000,30000,50000,100000]})
df9 = pd.merge(df0,df8, left_on = 'employee', right_on = 'name')
df9


# In[9]:


df9a = df9.set_index('employee')
df9a


# In[10]:


df9a.drop(['name'],axis=1, inplace=True)
df9a


# In[11]:


data1 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
                    'food': ['fish', 'beans', 'bread']})
                   
data2 = pd.DataFrame({'name': ['Mary', 'Joseph','Paul'],
                    'drink': ['wine', 'beer','grapewine']})
data1,    data2


# In[12]:


#inner join

data3 = pd.merge(data1,data2, how = 'inner')
data3


# In[13]:


#outer join

data4 = pd.merge(data1,data2, how = 'outer')
data4


# In[14]:


#left join

data5 = pd.merge(data1,data2, how = 'left')
data5


# In[15]:


#right join

data6 = pd.merge(data1,data2, how = 'right')
data6


# # GROUPBY

# In[16]:


fd0 = pd.read_excel(r"Downloads\Startup Trends Across India.xlsx")


# In[17]:


fd = pd.DataFrame(fd0)


# In[18]:


fd.head()


# In[19]:


fd.dtypes


# In[20]:


del fd['SNo']


# In[21]:


fd.head()


# In[22]:


fd.shape


# In[23]:


fd.set_index('Date')


# In[24]:


fd['CityLocation'].value_counts()


# In[25]:


#Group by function 

count = fd.groupby(['InvestmentType']).size()
print(count)


# In[26]:


#group by with 2 columns

count1 = fd.groupby((['InvestmentType','CityLocation'])).size().sort_values(ascending=False)
print(count1)


# In[27]:


max1 = fd.groupby(['CityLocation'])['AmountInUSD'].max()
max1


# In[ ]:




