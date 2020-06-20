#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. Voting Eligibility
age = int(input("Enter your age "))
if(age<18):
    print("OOPS! Not eligible for voting")
else:
    print("Congrats You are eligible for voting")


# In[6]:


#2. Even or Odd
num = int(input("Enter the number "))
a = num%2
if(a==0):
    print("The number is an EVEN number")
else:
    print("The number is an ODD number")


# In[10]:


#3. Reverse of  String
s = input("Enter the sting ")
a = s[::-1]
print("The reversed string is ",a)


# In[12]:


#4. Positive or not
num = float(input("Enter a number "))
if(num>0):
    print("The number entered is a POSITIVE number")
else:
    print("The number entered is NOT a POSITIVE number")


# In[ ]:


#5. Roots of a Quadratic Equation
z = print("Enter the the quadratic equation's terms respectively")
a=float(input("The constant term of x^2 " ))
b=float(input("The constant term of x " ))
c=float(input("The constant term "))
d = b**2-4*a*c
if(d>0):
    print("The roots are real and distant")
    print("The roots of the equation are ",(-b+d**0.5)/2*a,",",(-b-d**0.5)/2*a)
elif(d==0):
    print("The roots are real and equal")
    print("The root of the equation is ",-b/2*a)
else:
    print("The roots are imaginary")
    print("The roots of the equation are ",(-b+d**0.5)/2*a,",",(-b-d**0.5)/2*a)


# In[ ]:


#6. Check the number is posivite ,negative or zero
num = float(input("Enter a number "))
if(num>0):
    print("The number entered is a POSITIVE number")
else:
    if(num<0):
        print("The number entered is a NEGATIVE number")
    else:
        print("The number is 0")


# In[ ]:


#7. Take numbers and print in words
num = int(input("Enter a number in between 1 to 5 "))
if(num==1 or num==2 or num==3 or num==4 or num==5):
    print("Your number is in the range")
    if(num==1 or num==2 or num==3):
        if(num==1):
            print("Your number is ONE")
        elif(num==2):
            print("Your number is TWO")
        else:
            print("Your number is THREE")
    else:
        if(num==4):
            print("Your number is FOUR")
        else:
            print("Your number is FIVE")
else:
    print("Your number is out of the range")


# In[ ]:


#8. Vowel or NOT a Vowel
z = input("Enter a character ")
if(z=='A' or z=='E' or z=='I' or z=='O' or z=='U' or z=='a' or z=='e' or z=='i' or z=='o' or z=='u'):
    print(z, "is a Vowel")
else:
    print(z, "is a NOT a Vowel")


# In[ ]:




