#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Homework 1: Create logic!
nb, ng, nt =map(int,input().split())
b1=ng>25
b2=ng<=30
b3=nb>20 and  nt>2 or ng>30 and nt>4
b4=nb<60 or ng <70
b5=nb>=60 or ng>=70
b6=nb==ng+10
b7=abs(nb-ng) <10 or nt>5
b8= b6 or ng==nb+15

print(b1,b2,b3,b4,b5,b6,b7,b8)



# In[ ]:





# In[ ]:




