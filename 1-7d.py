#!/usr/bin/env python
# coding: utf-8

# In[2]:


n,m,l=map(int,input().split())
a=[]
b=[]
for i in range(n):
    a.append(list(map(int,input().split())))
for j in range(m):
    b.append(list(map(int,input().split())))
for i in range(n):
    c=[]
    for j in range(l):
        su=0
        for k in range(m):
            su+=a[i][k]*b[k][j]
        c.append(su)
    print(" ".join(list(map(str,c))))
    


# In[ ]:




