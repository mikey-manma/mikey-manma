#!/usr/bin/env python
# coding: utf-8

# In[2]:


n=int(input())
k=[[[0 for _ in range(10)]for _ in range(3)]for _ in range(4)]
for _ in range(n):
    b,f,r,v = map(int,input().split())
    k[b-1][f-1][r-1]+=v
for i in range(4):
    for j in range(3):
        print(" "+" ".join(map(str,k[i][j])))
    if(i != 3):
        print("#"*20)


# In[ ]:




