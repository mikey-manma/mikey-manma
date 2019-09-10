#!/usr/bin/env python
# coding: utf-8

# In[38]:


import sympy
a,b,c = input().split()
d = []
d = sympy.divisors(int(c))
e=1
f=0
g=len(d)
while(f<g):
    if(int(a)<d[f]<int(b)):
        e=e+1
    f=f+1
print(e)


# In[ ]:




