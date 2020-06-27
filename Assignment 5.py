#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Length of the string
a=input("Enter a string ")
b=len(a)
print("The length of the string is",b)


# In[ ]:


#2. Counting number of Characters
string = input("Enter a string ")  
add = {} 
  
for i in string: 
    if i in add: 
        add[i] += 1
    else: 
        add[i] = 1  
print ("Count of all characters"+ str(add)) 


# In[ ]:


#3. Getting a single string from two strings and swapping first two characters
a=input("enter the first string ")
b=input("enter the second string ")
c=a[0:2]
a=a.replace(a[0:2],b[0:2])
b=b.replace(b[0:2],c)
print("combined string after swapping of characters ")
print(a," ",b)


# In[ ]:


#4. Displaying strings in uppercase and lowercase
a=input("enter the string : ")
print("the string in upper case is ",a.upper())
print("the string in lowercase is ",a.lower())


# In[ ]:


#5. Removing a newline from a string
a=input("enter the string ")
print("the string is ",a)
a=a.rstrip("/n")
print("the string after removing newline is ",a)


# In[ ]:


#6. Counting the occurrences of substring
a=input("enter the string ")
b=input("enter the substring ")
count=a.count(b)
print("the no. of occurrences = ",count)


# In[ ]:


#7. Converting string in to a list
a=input("enter the string ")
for x in a:
    print(x)


# In[ ]:


#8. Program for deletion of a character
a=input("enter the string ")
i=int(input("enter the index of character you want to delete "))
a[:i]+a[(i+1):]


# In[ ]:


#9. Printing every character of a string
a=input("enter the string ")
for i in range(len(a)):
    print((b+1),".",a[b])


# In[ ]:


#10. Finding length ,length function
str="refrigerator"
count=0
for i in str:
    count=count+1
print("the length of string is : ",count)

