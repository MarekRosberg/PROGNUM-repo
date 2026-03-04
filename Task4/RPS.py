#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


input_rps = input("What do you want to play? R for Rock, S for Scissors, P for paper:")
print(input_rps) #Making sure the input is correct
    
possibilities = np.array(['R', 'P', 'S']) #Definitions for indexes of random numbers
#0 is Rock, 1 is Paper, 2 is Scissors
computer_p = np.random.randint(0, len(possibilities))
if input_rps=="R":
    if computer_p==0: #Rock-Rock
        print("It's a draw, try again")
    elif computer_p==2: #Rock-Scissors
        print("Good job, here is your prize: You can go home")
    else: #Rock-Paper
        print("Lol you lost")
elif input_rps=="P":
    if computer_p==1: #Paper-Paper
        print("It's a draw, try again")
    elif computer_p==0: #Paper-Rock
        print("Good job, here is your prize: You can go home")
    else: #Paper-Scissors
        print("Lol you lost")
elif input_rps=="S":
    if computer_p==2: #Scissors-Scissors
        print("It's a draw, try again")
    elif computer_p==1: #Scissors-Paper
        print("Good job, here is your prize: You can go home")
    else: #Scissors-Rock
        print("Lol you lost")
else: #Wrong Input
    print("Sideye")


# In[ ]:




