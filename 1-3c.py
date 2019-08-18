#!/usr/bin/env python
# coding: utf-8

# In[10]:


n=0
l = list(iter(input,"0 0"))
while(True):
    a=l[n][0]
    b=l[n][2]
    if(int(a)>int(b)):
        print(str(b)+" "+str(a))
    else:
        print(a+" "+b)
    n=n+1


# In[ ]:




