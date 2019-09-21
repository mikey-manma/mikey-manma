#!/usr/bin/env python
# coding: utf-8

# In[1]:


s=[1,2,3,4,5,6,7,8,9,10,11,12,13]
h=[1,2,3,4,5,6,7,8,9,10,11,12,13]
c=[1,2,3,4,5,6,7,8,9,10,11,12,13]
d=[1,2,3,4,5,6,7,8,9,10,11,12,13]
a=input()
for i in range(int(a)):
    x,y=input().split()
    if(b=="S"):
        s.remove(int(c))
    elif(b=="H"):
        h.remove(int(c))
    elif(b=="C"):
        c.remove(int(c))
    elif(b=="D"):
        d.remove(int(c))
print("S "+str(s[0:]))
print("H "+str(h[0:]))
print("C "+str(c[0:]))
print("D "+str(d[0:]))

