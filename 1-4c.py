#!/usr/bin/env python
# coding: utf-8

# In[11]:


import sys
a,b,c=input().split()
if(b=="+"):
    d=int(a)+int(c)
    print(d)
elif(b=="-"):
    d=int(a)-int(c)
    print(d)
elif(b=="*"):
    d=int(a)*int(c)
    print(d)
elif(b=="/"):
    d=int(a)/int(c)
    print(d)
elif(b=="?"):
    print()


# In[ ]:




