#!/usr/bin/env python
# coding: utf-8

# In[2]:


while True:
    H,W = map(int,input().split())
    if H+W==0:
        break
    for i in range(H):
        S = ""
        for j in range(W):
            if(i+j)%2==0:
                S += "#"
            else:
                S += "."
        print(S)
    print()


# In[ ]:




