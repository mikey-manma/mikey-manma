#!/usr/bin/env python
# coding: utf-8

# In[2]:


D=[
    (1,5,2,3,0,4),
    (3,1,0,5,4,2),
    (4,0,2,3,5,1),
    (2,1,5,0,4,3),
]
N=int(input())
L=[None]*N
for i in range(N):
    *L[i], = map(int,input().split())
p=(0,0,0,1,1,2,2,3)
ok=1
for i in range(N):
    Li=L[i]
    for j in range(i+1,N):
        Lj=L[j]
        for k in range(24):
            if Li == Lj:
                ok = 0
            Lj[:]=(Lj[e] for e in D[p[k%8]])
print("Yes" if ok else "No")


# In[ ]:




