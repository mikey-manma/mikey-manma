#!/usr/bin/env python
# coding: utf-8

# In[2]:


d=input().split()
s={"N":"152304","W":"215043","E":"310542","S":"402351"}
for o in input():
    d=[d[int(i)]for i in s[o]]
print(d[0])


# In[ ]:




