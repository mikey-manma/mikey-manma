#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(10000):
    h,w=map(int,input().split())
    if h+w==0:
        break
    print("#"*w)
    for j in range(h-2):
        print("#"+"."*(w-2)+"#")
    print("#"*w)


# In[ ]:




