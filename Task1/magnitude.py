#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Sirius data
apparentMagnitude = -1.46
absoluteMagnitude = 1.45

# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

m = apparentMagnitude
M = absoluteMagnitude

d1 = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164
a = input("apparent magnitude: ")
b = input("absolute magnitude: ")
x1 = float(a)
x2 = float(b)
print("The distance to the star with the apparent magnitude",x1, "and absolute magnitude",x2, "is", d1)
print("The distance of Sirius is 8.61")


# In[ ]:




