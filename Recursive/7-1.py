
# coding: utf-8

# Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent), write code to calculate the number of ways of representing n cents

# In[13]:

l=[0,0,0,0]
def calway(n,l, coin,r):
  if(n == 0):
    print(l)
    r.append(l)
    #return l
  if(n >= 25 and coin >= 25):
    l25=l[:]
    #a=n//25
    l25[-1]=l25[-1]+1
    b=n- 25
    calway(b, l25, 25,r)
    #q.append(s)
  if(n >= 10 and coin >=10):
    l10=l[:]
    #a=n//10
    l10[-2]=l10[-2]+1
    b=n -10
    calway(b, l10, 10,r)
    #q.append(s)
  if(n >=5 and coin >=5):
    l5=l[:]
    #a=n//5
    l5[1]=l5[1]+1
    b=n - 5
    calway(b, l5, 5,r)
    #q.append(s)
  if( n>=1 and coin >=1 ):
    l1=l[:]
    l1[0]=l1[0]+1
    b=n-1
    calway(b,l1, 1,r)
    #q.append(s)
    #print("aa",s)
  

  
  #print("ddddd",s)
  return r

a=calway(16,l, 25,[])
#print("salam")
print(a)


# In[ ]:




# In[ ]:



