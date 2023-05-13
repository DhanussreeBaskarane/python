#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("hello world")


# In[4]:


a=int(input("enter a value"))
b=int(input("enter a value"))
c=a+b
print("the sum is",c)


# In[12]:


a=int(input("Enter first number"))
b=int(input("Enter second number"))
print("a=",a)
print("b=",b)
a=a+b
b=a-b
a=a-b
print("after swapping")
print("a=",a)
print("b=",b)


# In[7]:


n=float(input("enter a number in km"))
c=n*0.62137119
print("in miles=",c)


# In[8]:


a=int(input("enter a no"))
if(a>0):
    print("positive")
elif(a<0):
    print("negative")
else:
    print("zero")


# In[9]:


n=int(input("enter a year"))
if((n%4==0)and(n%100!=0)or(n%400==0)):
    print("it is a leap year")
else:
    print("it is not a leap year")


# In[13]:


for n in range(1,30):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
            print(n)


# In[14]:


n1=0
n2=1
print(n1)
print(n2)
for n in range(0,50):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3


# In[17]:


n=int(input("Enter a number"))
sum=0
temp=n
while n>0:
    r=n%10
    sum=sum+(r*r*r)
    n=n//10
if temp==sum:
    print("Armstrong")
else:
    print("Not an armstrong no")


# In[18]:


n=int(input("Enter a number"))
c=0
for i in range(0,n):
    c=c+i
    i+=1
print(c)


# In[19]:


for i in range (0,6):
    print("*"*i)
    i+=1


# In[22]:


def remove_n_chars_from_start(string, n):
    return ''.join([string[i] for i in range(n, len(string))]) 
string = "hello world"
n = 3
new_string = remove_n_chars_from_start(string, n)
print(new_string)


# In[26]:


list2=[]
def divisible_by_5(list1):
   print("Given list",list1)
   for i in x:
       if i%5==0:
          list2.append(i)

x=[5,10,20,31,15,22]
divisible_by_5(x)
print("The list is",list2)


# In[28]:


str="hiwelcome,hi,hicat,"
str.count("hi")


# In[29]:


rows = 6
for i in range(rows):
    for j in range(i):
        print(i, end=' ')
    print('')


# In[30]:


n=int(input("enter the value"))
temp=n
sum=0
while(n>0):
    r=n%10
    sum=(sum*10)+r
    n=n//10
if(temp==sum):
    print("palindrome")
else:
    print("not a palindrome")


# In[31]:


list=[1,2,3,4,5]
list[0],list[-1]=list[-1],list[0]
print(list)


# In[33]:


def swapList(sl,pos1,pos2):
    n = len(sl)     
    temp = sl[pos1]
    sl[pos1] = sl[pos2]
    sl[pos2] = temp
    return sl      
l= [1,2,3,4,5,6]
pos1= 2
pos2= 5
print(l)
print("Swapped list:",swapList(l,pos1-1,pos2-1))


# In[35]:


list=[1,2,3,4,5,6]
print(len(list))


# In[36]:


a=7
b=6
if(a>b):
    print("a is greater")
else:
    print("b is greater")


# In[39]:


a=5
b=4
if(a<b):
    print("a is lesser")
else:
    print("b is lesser")


# In[41]:


string = 'amaama'
half = int(len(string) / 2) 
first_str = string[:half]
second_str = string[half:]
if first_str == second_str:
    print(string, 'string is symmetrical')
else:
    print(string, 'string is not symmetrical')
if first_str == second_str[::-1]: 
    print(string, 'string is palindrome')
else:
    print(string, 'string is not palindrome')


# In[42]:


list=['hello','cat','dog']
list.reverse()
print(list)


# In[43]:


test_str = "GeeksForGeeks"
new_str = test_str.replace('e', '')
print ("The string after removal of i'th character( doesn't work) : " + new_str)
new_str = test_str.replace('s', '', 1)
print ("The string after removal of i'th character(works) : " + new_str)


# In[44]:


str="welcome"
print(len(str))


# In[50]:


n="she is a girl"
s=n.split(" ")
for i in s:
    if len(i)%2==0:
        print(i)


# In[51]:


import sys
tup1= ("Studytonight", 1, 2, 3)
tup2= ("Python", "Java", "C++")
tup3= ((1, 2), (4, 6), (7, 2), (10, 9))
print("Size of tuple1: ", sys.getsizeof(tup1), "bytes")
print("Size of tuple2: ", sys.getsizeof(tup2), "bytes")
print("Size of tuple3: ", sys.getsizeof(tup3), "bytes")


# In[53]:


tup=(2,4,1,6,3)
print("Maximum element",max(tup))
print("Minimum element",min(tup))


# In[56]:


tup=(2,4,1,6,3)
print(sum(tup))


# In[57]:


test_list = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]
print("The original list is : " + str(test_list))
cus_eles = [6, 7, 8]
res = [[(idx, val) for idx in key] for key,  val in zip(test_list, cus_eles)]
print("The matrix after row elements addition : " + str(res))


# In[ ]:




