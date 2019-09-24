#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
a,b,c=map(float,input().split())
c=math.radians(c)
s=a*b*math.sin(c)/2
d=(a**2+b**2-2*a*b*math.cos(c))**0.5
h=b*math.sin(c)
print("{:.5f}".format(s))
print("{:.5f}".format(a+b+d))
print("{:.5f}".format(h))


# In[ ]:




