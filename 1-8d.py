#!/usr/bin/env python
# coding: utf-8

# In[2]:


s=input()
p=input()
s+=s
ans="No"
for i in range(len(s)//2):
    if(s[i]==p[0]):
        for j in range(len(p)):
            if(s[i+j]!=p[j]):
                break
            if(j==len(p)-1):
                ans="Yes"
print(ans)


# In[ ]:




