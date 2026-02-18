#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Dates for the first Julian date") #First Julian Statistics
Y1 = float(input("Year:"))
M1 = float(input("Month:")) #Month considered as 1-12, January 1, December 12
D1 = float(input("Day:"))

JD1 = 367*Y1 -7*(Y1+(M1+9)/12)/4 - 3*((Y1+(M1-9)/7)/100 + 1)/4 + (275*M1)/9 + D1 + 1721029-0.5 #Equation 1

print("Your first Julian date is:", JD1)

print("Dates for the second Julian date") #Second Julian statistics
Y2 = float(input("Year:"))
M2 = float(input("Month:"))
D2 = float(input("Day:"))

JD2 = 367*Y2 -7*(Y2+(M2+9)/12)/4 - 3*((Y2+(M2-9)/7)/100 + 1)/4 + (275*M2)/9 + D2 + 1721029-0.5 #Equation 2

print("Your second Julian date is:", JD2)

print("Difference is:", abs(JD1 - JD2)) 

Y3 = abs(JD1 - JD2)/365 #Calculating the amount of years

print("This equals to", Y3, "years")


# In[ ]:





# In[ ]:




