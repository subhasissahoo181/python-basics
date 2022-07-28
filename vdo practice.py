#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello")


# # Markdown
# 

# 
# # Arithmetic operation

# ### addition

# In[1]:


3+5


# In[3]:



[4,8]


# In[4]:


4+5


# In[5]:


4++8


# ### subtraction

# In[6]:


8-3


# In[7]:


4-9


# In[8]:


6.84-3.968


# ### multiplication

# In[9]:


5*6


# In[10]:


69*12


# In[11]:



5.25*6.7


# ### division

# In[12]:


4//5


# In[13]:


25/5


# In[14]:


3.141/7


# In[15]:


4.563//9.432


# ### exponent

# In[16]:


34^2


# In[17]:


5^5


# In[18]:


40^4


# In[19]:


3**2


# In[20]:


5**5


# In[21]:


1**5


# In[1]:


pow(5,5)


# ### madulus

# In[2]:


'''hello
silicon'''


# ## ffff

# # internship

# In[3]:


a=[1,2,3,4,5,'a',[1,2,3,4,5,'a'],34]


# In[4]:


print(a)


# In[6]:


len(a)


# In[7]:


print(id(a))


# In[8]:


a[7]


# In[9]:


A={'a':1,'b':2,'c':3,'d':4}


# In[10]:


A['b']


# In[3]:


pow(2,3)


# In[4]:


pow(3,2)


# In[5]:


pow(9,4)


# In[6]:


pow(5,2)


# In[9]:


10/3 


# In[12]:


10//3


# ### variable

# In[13]:


var=30


# In[14]:


var1=40


# In[15]:


print(var+var1)


# In[16]:


_data=20984


# In[17]:


print(_data)


# In[22]:


var1=29
   


# In[23]:


print(var1)


# In[36]:


Var=19
Var1_=30
1var=20
_var=22
_1Var=33
Var_1=5
.Var=98


# In[37]:


Var
Var1_
Var
_1Var
Var_1
Var


# ### Arirhmatic Operation

# In[38]:


x=2
y=3


# In[39]:


x+y


# In[41]:


x-y


# In[42]:


x*y


# In[43]:


x**y


# In[44]:


x/y


# In[45]:


pow(x,y)


# In[46]:


x//y


# In[47]:


x%y


# ### Data Type

# In[48]:


'''Integer 4,6,7,9
Float 5.4,3.5
Complex 3+4j,2j
Boolean True,False
String "Hello"
List [1,2,3,4,'hello,True']
Tuple(1,2,3,'hello',True)
Set {1,2,3,'Hello',True}
Dictionary {1:'sam',2:'sarah'}
'''


# In[49]:


x=10


# In[50]:


type(x)


# In[51]:


x='10'


# In[52]:


type(x)


# In[53]:


x=10.4


# In[54]:


type(x)


# In[56]:


x=True


# In[57]:


type(x)


# In[58]:


x=False


# In[59]:


type(x)


# In[60]:


x=2+4j


# In[61]:


type(x)


# In[62]:


x= [1,2,3,4,'Helo',"ram"]


# In[63]:


type(x)


# In[64]:


x=(1,2,3,4,'Hello',"Ram")


# In[65]:


type(x)


# In[66]:


x={1,2,3,4,"hello",'ram'}


# In[67]:


type(x)


# In[68]:


for countdown in 5,4,3,2,1,"hay!":
    print(countdown)


# In[71]:


spells=[
    "Riddikulus",
    "Wingardium leviosa!",
    "Avada"
    "Expect"
]


# In[73]:


print(spells[3])


# In[ ]:





# ### #Archive.py

# In[74]:


import webbrowser
import json
from urllib.request import urlopen

print("Let's find an old website.")
site= input("Type a website URL")
era = input("Type a year, month and day, like 20150613:")
url="http://archive.org/wayback/available?url=%s&timestamp=%s"%(site,era)
response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data=json.load(text)
try
old_site=data["archived_snapsorts"]["closest"]["url"]
print("Found this copy:",old_site)
print("it should apppear in your browser now.")
webbrowser.open(old_site)
except:
    print("Sorry, no luck finding ", site)


# In[1]:


char str[10] = "India",ch ='n'
int ind[10],loop,j=0
for(loop = 0; str[loop] != '\0'; loop=loop+1)
if(str[loop]==ch)
ind[j++]=loop
for(loop=0;loop<j;loop=loop+1)
print ind[loop]


# In[2]:


3+2


# ## Typecasting

# In[3]:


int(20)


# In[4]:


float(32)


# In[5]:


str(30)


# In[6]:


str('12.243')


# In[7]:


float('Hello')


# In[9]:


float(245.4)


# In[10]:


str('hello')


# In[11]:


int(12.45)


# In[12]:


int('12.45')


# In[13]:


float('12.45')


# In[14]:


str(12.45)


# In[15]:


int(float('12.45'))


# ## User Input

# In[16]:


input('number')


# In[17]:


input()


# In[18]:


input("Enter youe Age:")


# In[19]:


x = input("Enter your Age:")


# In[20]:


x


# In[21]:


x=int(input("Enter Your Age:"))


# In[22]:


x


# In[23]:


type(x)


# In[25]:


x=float(input("Enter your Age"))


# In[26]:


x


# In[29]:


type(x)


# ### Formating Print Statement

# In[36]:


x=int(input("Sam::Enter your Age:"))


# In[37]:


y=x+30


# In[38]:


print("Sam is",x,"years old and his father is",y,"Years old")


# In[39]:


print("Sam is {a} years old and his father is {b} year old".format(a=x,b=y))


# In[43]:


print("Sam is {0} year old and his father is {1} years old ".format(x,y))


# In[45]:


print("Sam is {}years old and his father is {} year old.".format(x,y))


# ### indentation

# In[46]:


'''function
if else
for 
while
class()
'''


# In[54]:


if(x>y):
    print("x is greater")
    
else:
        print("Y is greater")


# In[56]:


for i in range(0,10):
       if(i>3):
           print(i)


# #### Assignment Operator

# In[57]:


x=5


# In[58]:


x=+10


# In[59]:


print(x)


# In[60]:


x=x+10


# In[61]:


print(x)


# In[62]:


x=x-10


# In[63]:


print(x)


# In[65]:


x=x%10
print(x)


# In[68]:


x=5
x=x**3
print(x)


# In[69]:


x


# #### Relational Operator

# In[70]:


10<4


# In[71]:


4>2


# In[72]:


4<<20


# In[73]:


5<=9


# In[74]:


x=82
y=26
x<y


# In[75]:


x==10


# In[76]:


x==82


# In[77]:


x=82


# In[78]:


x!=20


# In[79]:


x!=82


# #Logical Operator

# #### Boolean Value

# In[1]:


True*True


# In[2]:


True*False


# In[3]:


False*False


# In[4]:


True+True


# In[5]:


True+False


# In[6]:


False+False


# In[7]:


True&True


# In[8]:


True&False


# In[9]:


False&False


# In[10]:


True|True


# In[11]:


True|False


# In[12]:


False|False


# ### If-Else Statement

# In[13]:


x=15


# In[18]:


if(x>5):
    print("x is greater than 5");


# In[19]:


if(x>15):
    print("X is greater than 15")


# In[20]:


if(x>=15):
    print("X is greater than 15")
else:
    print("X is less thean 15")


# In[21]:


if(x<=5):
    print("x is lesser than equal to 5")
elif((x>5)&(x<10)):
    print("x is between 5 and 10")
else:
    print("X is greater than equal to 10")


# In[22]:


if(x%2==0):
    print("X is even")
elif((x%5==0)or(x%7==0)):
    print("x can be divided")
else:
    print("x can not be divided")


# ## #List

# In[24]:


li=[1,2,3,5,3,7]


# In[25]:


li


# In[26]:


list=['sam','hari','gutu']


# In[28]:


list[2]


# In[29]:


li[5]


# In[30]:


li[-4]


# In[31]:


li[-1]


# In[32]:


len(li)


# In[35]:


type(li)


# In[38]:


len(li)


# ### List Slicing

# In[40]:


list1=['sam','john','sarah','kartik']


# In[41]:


list1[:]


# In[42]:


list1[:]=['sam','john','sarah','karthik']


# In[43]:


list1[0:]


# In[44]:


list1[1:]


# In[45]:


list1[2:]


# In[46]:


list1[3:]


# In[47]:


list1[4:]


# In[48]:


list1[1:3]


# In[49]:


list1[-1:-3]


# In[50]:


list11=['sam','john','sarah','karthik','jason','matt']


# In[51]:


list11[0:6:1]


# In[52]:


list11[::-1]


# In[53]:


'''
List.append()
List.extend([])
List.insert()
List.pop()
List.remove()
'''


# ### Append

# In[54]:


a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


# In[55]:


a


# In[56]:


a.append(33)


# In[57]:


a


# ### Extend

# In[58]:


a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


# In[59]:


a.extend([55,99])


# In[60]:


a


# ### Insert

# In[64]:


a.insert(-2,12)


# In[63]:


a


# In[65]:


a.pop(-2)


# In[66]:


a.pop(0)


# In[67]:


a


# In[68]:


a.remove(12)


# In[69]:


a


# In[70]:


a.count(12)


# In[71]:


a.count(9)


# In[72]:


a.index(17)


# In[73]:


a.reverse()


# In[74]:


a


# ### Sort

# In[75]:


a


# In[76]:


a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


# In[77]:


a


# In[78]:


a.sort()


# In[79]:


a


# In[80]:


a.sort(reverse = True)


# In[81]:


a


# ### length

# In[82]:


len(a)


# In[83]:


a.remove(12)


# In[84]:


len(a)


# ## String

# In[85]:


A="Hello Python Program"


# In[86]:


A[0]


# In[87]:


A[-1]


# #### String Slicing

# In[88]:


A


# In[89]:


A[:]


# In[90]:


A[0:]


# In[91]:


A[2:]


# In[92]:


A[:5]


# In[93]:


A[:-4]


# In[94]:


A[::-1]


# In[97]:


A[::1]


# ### String Method

# In[98]:


A.strip()


# In[99]:


A.lower()


# In[100]:


A.upper()


# In[105]:


A.replace('Program','Code')


# In[104]:


A.split()


# ### In and Not In Operator

# In[106]:


A="His Mark in Physics, Chemistry,History are 50, 60, 70."


# In[107]:


'50'in A


# In[108]:


'50'not in A


# ### use of Backslash

# In[110]:


a="He is a 'legend' in cricket."


# In[111]:


a


# In[112]:


a="He is a \"legend\" in cricket."


# In[113]:


a


# In[115]:


'\t'


# ### \t

# In[116]:


x="Hello\tWorld"


# In[117]:


x


# In[118]:


print(x)


# ### \n

# In[120]:


x="Hello\nWorld"


# In[121]:


x


# In[122]:


print(x)


# ### ForLoop

# In[124]:


for i in range(0,6):
    print("Hi Subhasis")


# In[125]:


x=1
for i in range(0,5):
    print(x+i)


# In[128]:


x=1
for i in range(0,5):
    print(x+i+i)


# ### Factorial Of a Number

# 

# In[134]:


x=1
for i in range(1,6):
    x=x*i
    print(x)


# In[135]:


x=10
for i in range(0,5):
    x=x-1
    print(i,x)


# In[138]:


y=int(input("please Enter A Number"))
x=1
for i in range(1,y+1):
    x=x*i
print(x)


# In[139]:


li=['Black','White','Blue','red']


# In[140]:


for i in li:
    print(i)


# In[141]:


for i in range(0,10):
    print(li[0])


# In[142]:


for i in range(0,len(li)):
    print(li[i])


# ### While Loops

# In[143]:


i=0
while(i<5):
    print("Hello")
    i=i+1


# In[146]:


i=0
while(i<5):
    print(i)
    i=i+2


# In[147]:


i=0
j=0
while(i+j<10):
    print(i,j)
    i=i+1
    j=j+2


# ### Break

# In[151]:


for i in range(1,5):
    if(i==3):
        break
    print(i)


# In[152]:


for i in range(0,10):
    if(i==3):
        print("i is 3")
        break
    print(i)


# In[153]:


l1=[10,20,304,40,50,60]
for i in l1:
    if i == 40:
        break
    print(i)


# ### Continue

# In[154]:


for i in range(1,5):
    if(i==3):
        continue
    print(i)


# In[155]:


for i in range(1,5):
    if i==3:
        print("we are skiping 3")
        continue
    print(i)


# In[1]:


l1=[10,20,30,40,50]
for i in l1:
    if i==30:
        print("Skipping 30")
        continue
    print(i)


# In[4]:


l2=[11,20,30,44,55,66]
for i in l2:
    if i==30:
        print("Skippig 30")
    if i==20:
        print("breaking the loop")
        break
    print(i)


# ### Function

# In[5]:


def square(x):
    y=x**2
    return(y)


# In[6]:


square(6)


# In[7]:


def cube(x):
    y=x**3
    return(y)


# In[8]:


cube(2)


# In[9]:


def addMul(x,y,z):
    add=x+y+z
    mul=x*y*z
    print("addition is",add)
    print("product is",mul)


# In[10]:


addMul(2,3,4)


# In[13]:


def addMul(x,y,z):
    add=x+y+z
    mul=x*y*z
    add="addition is",str(add)
    mul="multiplicaton is",str(mul)
    return(add,mul)


# In[14]:


addMul(2,3,4)


# In[15]:


type(addMul(2,3,4))


# ### factorial

# In[18]:


def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact = fact*i
    return(fact)


# In[19]:


factorial(4)


# ## Recursion

# In[20]:


#factorial
   


# In[21]:


def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)


# In[22]:


factorial(5)


# In[23]:


#Fibonacci Seriase


# In[31]:


def fibonacci(x):
    if(x==1):
        return 0
    elif(x==2):
        return 1
    else:
        return(fibonacci(x-1)+fibonacci(x-2))


# In[28]:


fibonacci(1)


# In[29]:


fibonacci(6)


# In[30]:


fibonacci(4)


# In[38]:


x = int(input("Enter No. for Fibonacci Series:"))
li=[]
for i in range(1,x+1):
    li.append(fibonacci(i))


# In[36]:


li


# In[39]:


li


# In[47]:


x = int(input("Enter No. for Fibonacci Series:"))
li=[]
for i in range(1,x+1):
    li.append(fibonacci(i))
str1 = ""
for i in li:
    str1 = str1 +" " + str(i)
print(str1)


# ## SET

# In[51]:


A = {10,2,3,"Hello",True,"Sam"}


# In[52]:


A


# In[53]:


B={True,False,'True','False',1,0,20,30,30.0,50,50.25}


# In[54]:


B


# In[55]:


type(B)


# In[56]:


c=set(B)


# In[57]:


for i in c:
    print(i)


# In[58]:


'''
thisSet.add(4)
thisSet.updae([4,5])
len(thisSet)
thisSet.remove(2)
thisSet.pop()
thisSet.clear()
'''


# In[59]:


Set={1,2,4,1,6,67,55,33,90,900,544}


# In[61]:


Set


# In[62]:


Set.add(10000)


# In[63]:


Set


# In[66]:


Set.update([330,550,60])


# In[67]:


Set


# In[68]:


len(Set)


# In[69]:


Set.update({33,30})


# In[70]:


Set


# In[71]:


Set.remove(33)


# In[72]:


Set


# In[73]:


Set.pop()


# In[74]:


Set.clear()


# In[75]:


len(Set)


# In[76]:


tuple(Set)


# In[77]:


c=tuple(Set)


# In[78]:


for i in Set:
    print(i)


# #### Tuple indexing

# In[80]:


tuple1=('Sam','John','Sarah','karthik')


# In[81]:


tuple1[0]


# In[82]:


tuple1[1]


# In[83]:


tuple1[2]


# In[85]:


tuple1[3]


# In[86]:


tuple1[4]


# In[87]:


tuple1[-1]


# In[89]:


tuple1[-2]


# In[90]:


tuple1[-3]


# In[91]:


tuple1[-4]


# In[93]:


tuple1[len(tuple1)-1]


# In[94]:


A=(10,20,30,40,50,60,20,40,30,10,20)


# In[95]:


len(A)


# In[96]:


A.count(A)


# In[97]:


A.count(20)


# In[98]:


A.index(20)


# # Dictionary

# In[115]:


student = {'john':75,'Mark':85,'Sarah':80,'Peter':98}


# In[100]:


student


# In[101]:


student['Sarah']


# In[102]:


type(student)


# In[103]:


for i in student:
       print(i,student[i])


# In[106]:


#For Only Values
for i in student.values():
    print(i)


# In[107]:


# for
for key,values in student.items():
    print(key,values)


# In[108]:


student = {'Mark' : [60,65,64,63,93],'Sarch':[82,83,84,85,87]}


# In[109]:


student


# In[111]:


for i in student:
    print(i,student[i])


# In[112]:


for i in student:
    for j in student[i]:
        print(i,j)


# ### Dictionary Method

# In[113]:


'''
len(Student)
del Student
del Student['john']
Student.pop('Gary')
Student.get('Martina')
'''


# In[116]:


student


# In[117]:


student.get('Sarah')


# In[118]:


for i in student:
       print(i,len(student[i]))


# ### Nested Dictionaries

# In[127]:


stud ={
    'john':{'history':85,'physics':98,'Chemistry':61,'Geography':88,'Mathematics':50},
    'Martina':{'history':75,'physics':96,'Chemistry':65,'Geography':82,'Mathematics':70},
    'Karthik':{'history':55,'physics':89,'Chemistry':64,'Geography':80,'Mathematics':58}
}


# In[128]:


stud


# In[136]:


stud['john']


# In[130]:


stud['john']['history']


# In[132]:


for i in stud:
    print(i,"got",stud[i]['history'],"Mark in History")


# In[137]:


for i in stud:
    print(i,len(stud[i]))


# In[4]:


for i in subjects:
    Marks = []
    for j in stud:
        Marks.append(stud[j][i])
    print(i,max(Marks))


# In[5]:


Subject=[]
for j in stud['karthik']:
    Subjects.append(j)


# ## Lambda Function

# In[6]:


def square(x):
    return(x*x)


# In[7]:


square(2)


# In[8]:


square_lambda = lambda x: x*x


# In[9]:


square_lambda(10)


# In[10]:


cube = lambda x: x**3


# In[11]:


cube(2)


# In[12]:


def addition(x,y):
    add = x+y
    return(add)


# In[13]:


addition(3,2)


# In[14]:


prod = lambda x,y:x*y


# In[15]:


prod(3,4)


# In[16]:


prod(2.5,3)


# In[17]:


def Greater(x):
    if x>15:
        print("Greater Than 15")
    else:
        print("Lesser")


# In[18]:


Greater(10)


# In[19]:


Greater(15)


# In[20]:


Greater(15.1)


# In[21]:


Larger = lambda x: "Greater than 15"if x>15 else "Lesser"


# In[22]:


Larger(21)


# In[23]:


Larger(12)


# In[27]:


def add(x,y):
    add = x+y
    if add>10:
        return(True)
    else:
        return(False)


# In[28]:


add(5,5)


# sum is greaterthan 10 = lambda x,y:True if x+y>10 else false

# #### Even Odd

# In[29]:


def even(x):
    if x%2 == 0:
        return("Even")
    else:
        return("Odd")


# In[30]:


even(4)


# In[31]:


even(3)


# In[33]:


odd = lambda x: 'odd' if x%2 !=0 else 'even'


# In[34]:


odd(4)


# In[35]:


odd(3)


# ## Map Function

# In[37]:


x=[1,2,3,4,5,6,7]
def square(x):
    return(x**2)
y=map(square,x)
list(y)


# In[38]:


def oddoreven(x):
    if(x%2==0):
        return("Even")
    else:
        return("Odd")


# In[39]:


y=map(oddoreven,x)


# In[40]:


list(y)


# # EXCEPTION HANDELING 

# In[45]:


try:
    print(xy)
except:
        print("Exception part will defined")


# In[46]:


x='Hello'
y=float(x)
print(y)


# In[47]:


x='Hello'
try:
    y=float(x)
    print(y)
except:
    print("Enter Number")


# In[49]:


x=12.25
try:
    y=float(x)
    print(y)
except:
    print("Enter Number")


# In[50]:


x='100'
try:
    y=float(x)
    print(y)
except:
    print("Enter Number")
finally:
    print("Finished...")


# In[52]:


x=input("Enter Age:")
y=int(x)+25


# In[53]:


try:
    x=input("Enter Age:")
    y=int(x)+25
    print(y)
except:
    print("Enter Number")
finally:
    print("Finish")


# In[55]:


def age():
    try:
        x=input("Enter Age:")
        y=int(x)+25
        print(y)
    except:
        print("Enter Number")
        age()
    finally:
        print("Finish")
age()


# In[61]:


x=2
y='hi'
try:
    print(x+y)
except TypeError:
    print("Only integers allowed")
finally:
    print("Finished...")


# In[64]:


x='hello'
try:
    print(int(x))
except ValueError:
    print("Only numbers allowed")
finally:
    print("Finished...")


# ## Zero Division Error

# In[66]:


x=2
y=0
try:
    print(x/y)
except ZeroDivisionError:
    print("Division by 0 is not allowed.")
finally:
    print("Finished...")


# ### Rise Exception

# In[71]:


l1=[1,2,3,4]
x=4
y=0
if x not in l1:
    raise Exception('Number Entered Not in List')
l1.index(x)
if y not in range(0,len(l1)-1):
    raise Exception("Index is not in range")
l1[y]


# In[ ]:




