#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input())
x=0
y=0
for i in range(n):
    a,b=input().split()
    if(a<b):
        y+=3
    elif a==b:
        x+=1
        y+=1
    else:
        x+=3
print(x,y)


# In[ ]:




