#!/usr/bin/env python
# coding: utf-8

# In[35]:


#1. Prints intyegers 1 to 100
for a in range(101):
    if a % 3 == 0 and a % 5 == 0:
        print("fizzbuzz")
        continue
    elif a % 3 == 0:
        print("fizz")
        continue
    elif a % 5 == 0:
        print("buzz")
        continue
    print(a)


# In[ ]:


#2. Remove consecutive duplicates from the list
a = list()
number = input("Enter the number of elements ")
print ('Enter numbers in array ')
for i in range(int(number)):
    n = input("number ")
    a.append(int(n))
old = None
new = []

for i in a:
    if i != old:
        new.append(i)
        old = i

print(new)


# In[12]:


#3. Finding Unique values
a = list()
number = input("Enter the number of elements ")
print ('Enter numbers in array ')
for i in range(int(number)):
    n = input("number ")
    a.append(int(n))
print ('array ',a)
print("Original List ",a)
b = set(a)
c = list(b)
print("List of unique numbers ",c)


# In[19]:


#4. Check whether the number is in range 
n=int(input('Enter the number '))
a=int(input(('Enter the lower range of which you want to check ')))
b=int(input(('Enter the upper range of which you want to check ')))      
def test_range(n):
    if n in range(a,b):
        print( "The number",n,"is in the range")
    else :
        print("The number is outside the given range ")
test_range(n)


# In[33]:


#5. Check whether the alphabet is upper or lowercase
string=input("Enter string ")
def k(string):
    add=0
    total=0
    a=0
    for i in string:
        if(i.islower()):
            add=add+1
        elif(i.isupper()):
            total=total+1
        else:
            a=a+1
    print("The number of lowercase characters are ")
    print(add)
    print("The number of uppercase characters are ")
    print(total)
    print("The number of characters which are neither uppercase nor lower case are ")
    print(a)
k(string)    


# In[ ]:





# In[ ]:





# In[ ]:




