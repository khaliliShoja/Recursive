
# coding: utf-8

# Implement an algorithm to print all valid (e.g., properly opened and closed) combinations of n-pairs of parentheses.

# In[3]:

l=[3,0,0]
c=""

def param(l,c):
  if(l[1]==l[0] and l[2]==l[0]):
    print(c)
    #print("salam")
    return
  
  elif(l[1] >= l[2]):
    if(l[1]==l[0]):
      c1=c[:]
      a1=l[:]
      a1[2]=a1[2]+1
      c1=c1+'b'
      param(a1,c1)
    else:
      c2=c[:]
      a2=l[:]
      a2[1]=a2[1]+1
      c2=c2+('a')
      param(a2,c2)
      a3=l[:]
      a3[2]=a3[2]+1
      c3=c[:]
      c3=c3+('b')
      param(a3,c3)


param(l,c)


# In[ ]:



