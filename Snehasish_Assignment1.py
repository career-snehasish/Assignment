#!/usr/bin/env python
# coding: utf-8

# Install Jupyter notebook and run the first program and share the screenshot of the output.
# 

# In[2]:


A= 'This is my First Program'

print (A)


# 2.
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple
# of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
# comma-separated sequence on a single line.

# In[47]:


A=[]

for i in range(2000,3200,1):
    if i%7==0 and i%5!=0:
        A.append(i)
print (*A, sep=',')


# 3.
# Write a Python program to accept the user's first and last name and then getting them printed in
# the the reverse order with a space between first name and last name.

# In[52]:


First_Name = input("Enter your First Name ")

Last_Name = input("Enter your last Name ")

Full_Name = print("Full Name is ", First_Name," " ,Last_Name)

Full_Name

rev_name=print("Reverse Name is ", Last_Name[::-1]," ",First_Name[::-1])

rev_name


# Write a Python program to find the volume of a sphere with diameter 12 cm.

# In[51]:


pi = 3.1415926535897931
d= 12
r=d/2
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)


# # Task 2

# In[57]:


A=input("enter values with comma separated ")

list=A.split(',')

print('list : ',list)


# In[63]:


n=5

for i in range (1,n+1,1):
    print('*'*i)
for i in range (n+1,0,-1):
    print('*'*i)  
    
    


# 3.
# Write a Python program to reverse a word after accepting the input from the user.

# In[64]:


Input_word = input("Enter Word ")

Correct_Word = print("Correct Word is ", Input_word)

Correct_Word

Rev_Word = print("Reverse Word is ", Input_word[::-1])

Rev_Word

