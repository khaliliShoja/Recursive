
# coding: utf-8

# Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent), write code to calculate the number of ways of representing n cents

# In[11]:

l=[0,0,0,0]
def calway(n,l, coin):
  if(n == 0):
    
    print(l)
    return l
  if(n >= 25 and coin >= 25):
    l25=l[:]
    #a=n//25
    l25[-1]=l25[-1]+1
    b=n- 25
    s=calway(b, l25, 25)
  if(n >= 10 and coin >=10):
    l10=l[:]
    #a=n//10
    l10[-2]=l10[-2]+1
    b=n -10
    s=calway(b, l10, 10)
  if(n >=5 and coin >=5):
    l5=l[:]
    #a=n//5
    l5[1]=l5[1]+1
    b=n - 5
    s=calway(b, l5, 5) 
  if( n>=1 and coin >=1 ):
    l1=l[:]
    l1[0]=l1[0]+1
    b=n-1
    s=calway(b,l1, 1)
  


# In[12]:

calway(16,l, 25)


# In[ ]:



