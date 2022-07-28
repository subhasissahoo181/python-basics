#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a=np.array([1,2,3])
b=np.array([1,2,3])
print(a)
print(b)


# In[2]:


b[1]=5


# In[3]:


b


# In[4]:


import numpy as np
c=np.array([[1,2,3],[4,5,6]])
print(c)


# Ndarray Object
# *Most important object defined in NumPy in an N-dimensional array type called ndarray.
# *Describes the collection of items of the same type.
# *Items can be accessed using a zero-based index.
# *Every item in an ndarray takes the same size of block in the memory.
# *Each element in ndarray is an object of data-type object(called dtype)

# In[7]:


#initializing Numpy array


# In[9]:


import numpy as np
np.zeros((3,4))


# In[11]:


import numpy as np
np.arange(10,25,5)


# In[12]:


import numpy as np
np.arange(10,20,2)


# In[15]:


import numpy as np
np.arange(6,17,3)


# In[16]:


import numpy as np
#startnum till endnum-interval
np.linspace(5,6,10)


# In[17]:


#Filling SAME number in a array of dimension x X y


# In[18]:


import numpy as np
#np.linspace((startnum,endnum,numberof points))
np.full((2,2),5)


# In[19]:


import numpy as np
np.full((2,4),6)


# In[24]:


import numpy as np
np.random.random((2,3))


# *ndarray.shape
# "Returns a tuple consisting of array dimensions. Can also be used to resize the array."
# 

# In[25]:


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a.shape)


# In[27]:


import numpy as np
a=np.array([[1,2,3,4],[4,5,6,4],[2,1,5,6]])
print(a.shape)


# In[28]:


a=np.array([[1,2,3],[4,5,6]])


# In[29]:


print(a)


# In[31]:


#np.array.shape return tuple(rownum,colnum)
print(a.shape)


# In[36]:


a.shape=(3,2)
#number of row
print(a.shape[0])
# number of column
print(a.shape[1])
print(a)


# "Returns a tuple consisting of array dimensions. Can also be used to resize the array."

# In[37]:


#This resizes the ndarray
import numpy as np
a=np.array([[1,2,3,4],[4,5,6,7]])
a.shape=(8,1)
print(a)


# In[38]:


"Returns the count of number of elements in an array."


# In[39]:


import numpy as np
a=np.arange(24)
print(a.size)


# In[40]:


a.size


# In[41]:


a


# In[42]:


a.dtype


# In[44]:


b=np.linspace(5,7,11)
print(b)
print(b.dtype)


# # Addition using Numpy

# In[45]:


import numpy as np
np.sum([10,20])


# In[47]:


a,b=10,20
np.sum([a,b])


# In[48]:


np.sum([[0,1],[0,5]],axis=0)


# In[49]:


np.sum([[0,1],[0,5]],axis=1)


# Other sililar operations that you can perform:
#     *np.subtract(a,b) #a-b
#     *np.divide(a,b)#a/b
#     *np.multiply(a,b)#a*b
#     *np.exp(a) #e^a
#     *np.sqrt(a)
#     *np.sin(a)
#     *np.cos(a)
#     *np.log(a)
#     

# In[51]:


a=np.array([5,10])
np.sum(a)


# In[54]:


b=np.array([2,3])
print(np.sum([a,b]))
print(np.subtract(a,b))


# In[55]:


a=[1,2,3]
b=[3,2,3]
print(np.equal(a,b))
print(np.array_equal(a,b))


# # Array Comparision 

# #### Element-wise Comparision

# In[56]:


import numpy as np
a=[1,2,4]
b=[2,4,4]
c=[1,2,4]
np.equal(a,b)


# In[58]:


import numpy as np
a=[1,2,4]
b=[2,4,4]
c=[1,2,4]
np.equal(a,c)


# In[59]:


import numpy as np
a=[1,2,4]
b=[2,4,4]
c=[1,2,4]
np.array_equal(a,b)


# ## Aggregate functions

# In[61]:


import numpy as np
a=[1,2,4]
b=[2,4,4]
c=[1,2,4]
print(np.sum(a))#Array wise sum
print(np.min(a)) #Min of an array
print(np.mean(a)) #Mean of the array
print(np.median(a)) #median of the array
print(np.corrcoef(a)) #correlation coefficient of array
print(np.std(a)) #Standard Deviation of array


# # Numpy Broadcasting

# ### Concept of Broadcasting

# In[62]:


import numpy as np
a=np.array([[0,0,0],[10,10,10],[20,20,20],[30,30,30]])
b=np.array([0,1,2])

print('First array:\n',a,'\n')
print('Second array:\n',b,'\n')
print('First Array +Secondarray \n',a+b)


# # Array Manipulation

# ##### Concatenating two arrays together

# In[63]:


np.concatenate((a,b), axis=0)


# In[64]:


np.vstack((a,b))


# In[65]:


np.hstack((a,b))


# In[66]:


np.coumn_stack((a,b))


# In[2]:


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a)
b=np.array([[3,4,5],[5,6,7]])
print(b)
print(np.concatenate([a,b],axis=0))
print(np.concatenate([a,b],axis=1))


# In[3]:


print(np.stack((a,b),axis=0))


# In[4]:


print(np.stack((a,b),axis=1))


# In[5]:


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[2,3,4],[5,6,7]])
print(np.stack((a,b),axis=0))
print("Horizontal Stack...")
print(np.hstack((a,b)))
print("Horizontal Concat...")
print(np.concatenate((a,b),axis=0))
print("Vertical Stack...")
print(np.vstack((a,b)))
print("Vertical Concat...")
print(np.concatenate((a,b),axis=1))


# In[10]:


import numpy as np
np.column_stack((a,b))


# #### Splitting Arrsy

# In[11]:


import numpy as np
x=np.arange(16.0).reshape(4,4)
print(x,"\n\n")
print(np.hsplit(x,2),"\n\n")
print(np.hsplit(x, np.array([3,6])))


# In[12]:


print(np.split(a,[1,2],axis=1))


# In[13]:


a[:,:1]


# In[14]:


a[:,1:2]


# In[15]:


a[:,2:]


# ## Advantages of Numpy Over a List

# In[21]:


#Numpy vs List :Memory size
import numpy as np
import sys
#define a list
l=range(1000)
print("Size of list:",sys.getsizeof(l)*len(l))

#define a numpy array
a=np.arange(1000)
print("Size of an array:",a.size*a.itemsize)


# In[24]:


#Numpy vs List: Speed
import time
def using_list():
    t1=time.time() #Starting/Initial Time
    x=range(10000)
    y=range(10000)
    z=[x[i]+y[i] for i in range(len(x))]
    return time.time()-t1
def using_Numpy():
    t1=time.time() #Starting/Initial Time
    a=np.arange(10000)
    b=np.arange(10000)
    z=a+b #more Convient than a list
    return time.time()-t1
list_time=using_list()
numpy_time=using_Numpy()
print(list_time,numpy_time)
print("In this example Numpy is "+str(list_time/numpy_time)+"times faster than a list")


# In[ ]:


#Numpy  vs List: Memory size
import numpy as np
im

