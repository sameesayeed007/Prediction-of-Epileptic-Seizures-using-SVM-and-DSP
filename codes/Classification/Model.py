#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import normalize
from sklearn.metrics import accuracy_score
import pickle
model = SVC(kernel='linear')
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))


# In[ ]:




