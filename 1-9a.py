#!/usr/bin/env python
# coding: utf-8

# In[2]:


W = input().lower()
ans=0
while True:
    T=input()
    if(T=="END_OF_TEXT"):
        break
    ans+=T.lower().split().count(W)
print(ans)


# In[ ]:




