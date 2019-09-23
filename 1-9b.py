#!/usr/bin/env python
# coding: utf-8

# In[1]:


while True:
    s=input()
    if(len(s)==1):
        break
    for _ in range(int(input())):
        a=int(input())
        s=s[a:]+s[:a]
    print(s)


# In[ ]:




