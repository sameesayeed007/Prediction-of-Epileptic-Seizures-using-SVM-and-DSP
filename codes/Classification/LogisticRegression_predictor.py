#!/usr/bin/env python
# coding: utf-8

# In[352]:


import pandas as pd 
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import normalize
from sklearn.metrics import accuracy_score
import pickle
from sklearn.linear_model import LogisticRegression
filename = 'finalized_modelLR.sav'
svclassifier = pickle.load(open(filename, 'rb'))


# In[353]:


file = 'chb10_38S.csv'
n = file[:9]
n=n+'HLR'
dff= pd.read_csv(file)
s=shuffle(dff)
print(s.head())
shuffled_file=n+'.csv'
s.to_csv(shuffled_file)
print(shuffled_file)


# In[354]:


dfff= pd.read_csv(shuffled_file)
print(dfff)


# In[355]:


first= dfff.iloc[0:108,:]
second=dfff.iloc[108:216,:]
third=dfff.iloc[216:324,:]
fourth = dfff.iloc[324:432,:]
fifth = dfff.iloc[432:,:]

frames5=[first,second,third,fourth]
result5=pd.concat(frames5)
#print(result5)
testFrame5=[fifth]
test5 = pd.concat(testFrame5)
#print(test5)
X_train =result5.iloc[:,2:71]
y_train = result5['class']


X_test = test5.iloc[:,2:71]
y_test = test5['class']

#X_train=normalize(X_train)
#X_test=normalize(X_test)

#print(X_train)


svclassifier.fit(X_train, y_train)
y_pred5 = svclassifier.predict(X_test)

sc5=svclassifier.score(X_test, y_test)
real=test5.iloc[:,71]
conv_arr= real.values
sc55=accuracy_score(conv_arr, y_pred5)

print(sc5)
print(sc55)


# In[356]:


frames4=[first,second,third,fifth]
result4=pd.concat(frames4)

testFrame4=[fourth]
test4 = pd.concat(testFrame4)

X_train =result4.iloc[:,2:71]
y_train = result4['class']

X_test = test4.iloc[:,2:71]
y_test = test4['class']

#X_train=normalize(X_train)
#X_test=normalize(X_test)


svclassifier.fit(X_train, y_train)
y_pred4 = svclassifier.predict(X_test)

sc4=svclassifier.score(X_test, y_test)
real=test4.iloc[:,71]
conv_arr= real.values
sc44=accuracy_score(conv_arr, y_pred4)

print(sc4)
print(sc44)


# In[357]:


frames3=[first,second,fourth,fifth]
result3=pd.concat(frames3)

testFrame3=[third]
test3 = pd.concat(testFrame3)

X_train =result3.iloc[:,2:71]
y_train = result3['class']

X_test = test3.iloc[:,2:71]
y_test = test3['class']

#X_train=normalize(X_train)
#X_test=normalize(X_test)


svclassifier.fit(X_train, y_train)
y_pred3 = svclassifier.predict(X_test)

sc3=svclassifier.score(X_test, y_test)
real=test3.iloc[:,71]
conv_arr= real.values
sc33=accuracy_score(conv_arr, y_pred3)

print(sc3)
print(sc33)


# In[358]:


frames2=[first,third,fourth,fifth]
result2=pd.concat(frames2)

testFrame2=[second]
test2 = pd.concat(testFrame2)

X_train =result2.iloc[:,2:71]
y_train = result2['class']

X_test = test2.iloc[:,2:71]
y_test = test2['class']

#X_train=normalize(X_train)
#X_test=normalize(X_test)


svclassifier.fit(X_train, y_train)
y_pred2 = svclassifier.predict(X_test)

sc2=svclassifier.score(X_test, y_test)
real=test2.iloc[:,71]
conv_arr= real.values
sc22=accuracy_score(conv_arr, y_pred2)

print(sc2)
print(sc22)


# In[359]:


frames1=[second,third,fourth,fifth]
result1=pd.concat(frames1)

testFrame1=[first]
test1 = pd.concat(testFrame1)

X_train =result1.iloc[:,2:71]
y_train = result1['class']

X_test = test1.iloc[:,2:71]
y_test = test1['class']

#X_train=normalize(X_train)
#X_test=normalize(X_test)


svclassifier.fit(X_train, y_train)
y_pred1 = svclassifier.predict(X_test)

sc1=svclassifier.score(X_test, y_test)
real=test1.iloc[:,71]
conv_arr= real.values
sc11=accuracy_score(conv_arr, y_pred1)

print(sc1)
print(sc11)


# In[360]:


predvalues=[]
predvalues=list(y_pred1)+list(y_pred2)+list(y_pred3)+list(y_pred4)+list(y_pred5)

index_list = dfff["index"].tolist()
d = {'Index':index_list,'Predicted_values':predvalues}
df = pd.DataFrame(d)

df = df.sort_values(by ='Index' )

original=[]
for i in range (360):
    original.append(0)
for j in range (180):
    original.append(1)
print(len(original))
df['original'] = original
print(df)
m=n+'C'
main_file = m+'.csv'

df.to_csv(main_file)

counter=0

for i in range(540):
    if( df.iloc[i,1]== df.iloc[i,2]):
        counter=counter+1
        
avg=counter/540
print(avg)


# In[ ]:




