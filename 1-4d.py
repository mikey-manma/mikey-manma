#!/usr/bin/env python
# coding: utf-8

# In[10]:


a=input()
b=input().split()
g=0
h=0
while(h<int(a)):
    g=g+int(b[h])
    h=h+1
c=max(b)
d=min(b)
print(str(d)+" "+str(c)+" "+str(g))


# In[ ]:




