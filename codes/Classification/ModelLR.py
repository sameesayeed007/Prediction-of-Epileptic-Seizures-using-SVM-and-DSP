#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import normalize
from sklearn.metrics import accuracy_score
import pickle
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
filename = 'finalized_modelLR.sav'
pickle.dump(model, open(filename, 'wb'))


# In[ ]:




