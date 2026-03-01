#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import sqrt
print("Quadratic equation is set as: ax^2 + bx + c")
a = float(input("first root (a):"))
b = float(input("second root (b):"))
c = float(input("constant (c):")) #Inputting all numbers

D = b**2-4*a*c #Setting the discriminant
if D > 0:
    x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b-sqrt(b**2-4*a*c))/(2*a) #Two roots, same for if and elif
    print("Equation has these 2 roots:", float(x1), float(x2))
elif D == 0:
    x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b-sqrt(b**2-4*a*c))/(2*a)
    print("Equation has 2 same roots, that equal", float(x1))
else: #In case D<0
    print("Equation has imaginary roots, thus I won't evaluate it.")


# In[ ]:




