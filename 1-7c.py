#!/usr/bin/env python
# coding: utf-8

# In[1]:


r,c=map(int,input().split())
a=[]
rsum=[]
for i in range(r):
    a.append(list(map(int,input().split())))
    a[i].append(sum(a[i]))
for i in range(r):
    print(" ".join(list(map(str,a[i]))))
csum=[]
for j in range(c+1):
    s=0
    for i in range(r):
        s+=a[i][j]
    csum.append(s)
print(" ".join(list(map(str,csum))))


# In[ ]:




