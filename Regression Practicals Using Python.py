#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


Age=np.array([22,19,23,31,21,41,27,26,18,34,31,28,24,20,21,19,35])
Height=np.array([175,152,165,162,193,137,182,162,172,160,172,160,163,185,190,168,137])
DBP=np.array([60,70,82,90,68,76,76,62,74,76,70,80,62,78,76,68,60])
SBP=np.array([122,102,118,108,120,104,120,116,118,102,112,122,118,124,120,102,106])
Volume=np.array([3.1,3.4,3,3.2,4.9,2.4,4.5,3.1,4.4,2.9,4.2,3,3,4.7,4.8,4.1,2.3])
df=pd.DataFrame({'Age':Age,'Height':Height,'DBP':DBP,'SBP':SBP,'Volume':Volume})
df


# In[15]:


sns.pairplot(df)
plt.title('Multiple Scatter Plot')


# In[9]:


from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm


# In[11]:


model=ols('Volume~ Age + Height + DBP + SBP',data=df).fit()
anova_lm(model)


# In[12]:


model.summary()


# In[13]:


model.predict(df.drop('Volume',axis=1))


# In[ ]:




