#!/usr/bin/env python
# coding: utf-8

# In[1]:


cards = []
k=["S","H","C","D"]
n=int(input())
for i in range(n):
    s,r=input().split()
    r=int(r)
    if(s=="S"):
        cards.append(0+r)
    elif(s=="H"):
        cards.append(13+r)
    elif(s=="C"):
        cards.append(26+r)
    elif(s=="D"):
        cards.append(39+r)
for i in range(1,53):
    if not(i in cards):
        print(k[(i-1)//13],(i-1)%13+1)


# In[ ]:




