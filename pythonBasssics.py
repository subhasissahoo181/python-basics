#!/usr/bin/env python
# coding: utf-8

# Intro to Python with Jupyter Notebook
# 

# In[1]:


print("Hello World")


# In[2]:


if 5>3:
    print("Five is greater than Three !")


# In[4]:


if 5>3:
    
    print("Five is greater then Three!")


# In[6]:


if 5>2:
    print("Five is greater then two!")
if 5>3:
        print("Five is greater than three")


# In[8]:


if 4>2:
    print("Four is greater than Two")
    
    print("Two is not greateeer than Four")


# In[9]:


x=5
y="Hello, World!"


# In[10]:


#hello moto


# In[11]:


print(x)
print(y)


# In[12]:


x=5
y="chandaan"


# In[13]:


print(x)
print(y)


# In[14]:


x=4
x="Subhasis"


# In[15]:


print(x)


# In[16]:


x = str(3)
y=int(3)
z=float(3)


# In[17]:


print(x)
print(y)
print(z)


# In[18]:


x=5
y = "Chandan"
print(type(x))
print(type(y))


# In[19]:


print(type(x))
print(type(y))


# In[20]:


x="Chandan"
# Is the same as the 
x='Chandan'


# In[21]:


pprint(x)


# In[22]:


x="john"
print(x)
#double quotes are the same as single quotes:
x='john'
print(x)


# In[23]:


a=4
A="sallay"


# In[24]:


print(a)
print(A)


# In[25]:


myvar ="john"
my_var = "john"
_my_var="john"
myVar="John"
MYVAR = "john"
myvar2="John"


# In[30]:


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)


# In[32]:


2myvar="john"
my-vaar="john"
my var="john"


# In[33]:


x,y,z ="orange","banana","cherry"


# In[34]:


print(x)
print(y)
print(z)


# In[35]:


x=y=z="Apple"
print(x)
print(y)
print(z)


# In[36]:


fruits = ["Apple","Banana","Cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)


# In[37]:


x= "awesome"
print("Python is "+x)


# In[38]:


x = "Python is "
y = "Awesome"
z = x+y
print(z)


# In[39]:


x=5
y=4
z=x+y
print(z)


# In[40]:


x=10
y=15
print(x+y)


# In[60]:


# x="Chandan is "
# y=21
# z="Year's Old"

# p=x+y+z
# print(p)


# In[43]:


x = "awesome"
def myFunc():
    print("Python ia "+x)
    myFunc


# In[44]:


myFunc()


# In[53]:


x ="awesome"

def myfunc():
    x= "fantastic"
    
    print("Python is "+ x)
    
    myfunc()
    
print("Python is not"+x)


# In[61]:


# # def myfunc():
# #     global x
#     x = "fantastic"
    
# #     myfunc()
    
#     print("python is "+ x)


# In[63]:


# x = "awesome"

# def myfunc():
#     global x
#     x = "fantastic"
    
#     myfunc()
    
#     print("Python is"+ x)


# Data Type
# 

# In[64]:


x="Hello World"
print(x)


# In[65]:


x=20
print(x)


# In[67]:


x=20.5
print(x)


# In[68]:


x= 1j
print(x)


# In[69]:


x=["apple","banana","Cherry"]
print(x)


# In[71]:


x=("apple","banana","cherry")
print(x)


# In[72]:


x=range(6)
print(x)


# In[73]:


x={"name": "john", "age": 36}
print(x)


# In[74]:


x = {"apple", "banana","Cherry"}
print(x)


# In[75]:


x = frozenseet({"apple","banana","cherry"})
print(f)


# In[1]:


x,y,z = "orange", "apple", "banana"
print(x,y,z)


# In[3]:


fruits = ["apple","orange","banana"]
x,y,z=fruits
print(x,y,z)


# # globalvariable

# In[4]:


x = "awesome"

def myfunc():
    print("Python is "+x)
    myfunc()


# In[ ]:


print(myfunc())


# In[1]:


x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


# In[2]:


x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is "+ x)
myfunc()

print("Python is " + x)


# In[3]:


def  myfunc():
    global x
    x = "fantastic"
    
myfunc()
print("python is " + x)


# In[10]:


x = "awesome"
 
def myfunc():
    global x
    x = "fantastic"
     
    myfunc()
    print("Python is +"+ x)


# In[ ]:




