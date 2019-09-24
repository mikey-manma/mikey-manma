#!/usr/bin/env python
# coding: utf-8

# In[4]:


s=input()
q=int(input())
r=[input().split() for _ in range(q)]
for t in r:
    a,b=int(t[1]),int(t[2])+1
    if t[0]=="replace":
        p=t[3]
        s=s[:a]+p+s[b:]
    elif(t[0]=="reverse"):
        s=s[:a]+s[a:b][::-1]+s[b:]
    elif(t[0]=="print"):
        print(s[a:b])


# In[ ]:




