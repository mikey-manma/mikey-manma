#!/usr/bin/env python
# coding: utf-8

# In[2]:


s = input()
lc=s.lower()
uc=s.upper()
ans=""
for i in range(len(s)):
    if s[i]==lc[i]:
        ans+=uc[i]
    else:
        ans+=lc[i]
print(ans)


# In[ ]:





# In[ ]:




