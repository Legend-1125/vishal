#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Area of Circle
import math
r = float(input("Enter the radius of the circle "))
a = math.pi*r**2
print("The area of the circle is",a)


# In[ ]:


#2. Area of Regular Polygon
import math
n = int(input("Number of sides of the polygon "))
if(n>2):
    s = int(input("Lenth of the side "))
    a = (n*s**2)/4*(math.tan(math.pi/n))
    print("The area of the polygon is ",a)
else:
    print("THe given input does'nt form a polygon")


# In[ ]:


#3. Area of a Segment
import math
r = float(input("Enter the radius of the circle "))
o = float(input("Enter the angle "))
if(o>360 or o<0):
    print("Angle is not possible")
else:
    a = (math.pi*(r*r)*(o/360)) - (1/2*(r*r)*math.sin((o*math.pi)/180)) 
    print("Area of the minor segment is",a)
    b = 360-a
    print("Area of the major segment is",b)
    


# In[ ]:


#4. Random number form list
import random
print("The random number from the list")
print(random.choice([100,1,2,3,30,40]))


# In[ ]:


#5. Generating random number
import random
print("The random number from the list")
print(random.randrange(1,10000,50))


# In[ ]:


#6. Programs using Math module 
import math
#1
      print("sin(60) is",(math.sin(60))
#2
      print("cos(pi) is",math.cos(math.pi))
#3
      print("tan(90) is",(math.tan(90)))
#4
      print("Angle of sin(0.8660254037844386) is",math.degrees(math.asin(0.8660254037844386)))      
#5
      print("5^8 is",5**8)  
#6
      print("Square root of 400",math.sqrt(400))      
#7
      print("5^e is",5**math.e)      
#8
      print("log(1024),base 2 is",math.log(1024,(2)))   
#9
      print("log(1024),base 10 is"math.log(1024,(10)))
#10
      print("FLoor of 23.56 is",math.floor(23.56))
      print("Ceiling of 23.56",math.ceil(23.56))      
      
      

