#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

input_func = input("Desired function letter:")
a = float(input("Lower boundary:"))
b = float(input("Higher boundary:"))

def integral(input_func, x, y):
    x = np.random.uniform(a, b, 100000)
    y = eval(input_func)
    
    intg = (b - a) * np.mean(y)
    
    return intg
print(f'{integral(input_func, a, b): .3f}')


# In[ ]:




