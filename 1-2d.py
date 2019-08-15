#!/usr/bin/env python
# coding: utf-8

# In[4]:


wide,high,x,y,r=input().split()
if(int(wide)<int(x)+int(r) or int(high)<int(y)+int(r) or 0>int(x)-int(r) or 0>int(y)-int(r)):
    print("No")
else:
    print("Yes")


# In[ ]:





# In[ ]:




