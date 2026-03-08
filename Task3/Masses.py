#!/usr/bin/env python
# coding: utf-8

# In[6]:


masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e+22]
Mmoon = 7.349e+22 #Mass of the Moon
newmasses = []
b = slice(6,11)
last5 = masses[b]
for M in masses:
    if M > 7.349e+22:
        newmasses.append(M) #Remove masses smaller than the Moon
   
print(newmasses)
a = slice(6, 11) #Slicing
print(last5)
avg = sum(last5)/len(last5) #Calculating the average
print("Average of the last 5 masses:", avg)
b = (3.3022e+23 + 7.349e+22 + 4.8685e+24 + 6.4185e+23 + 1.25e+22)/5
print("Test:", b) #Test


# In[ ]:




