
# coding: utf-8

# Write a method to compute all permutations of a string

# In[1]:

str1='abc'


def permSt(str1):
  if(len(str1)==1):
    return [str1] # No difference if you return str1
  
  
  l=[]
  for i in range(0, len(str1)):
    
    if(i==len(str1)-1):
      k1=str1[:i]
    else:
      k1=str1[:i]+str1[i+1:]
    l1=permSt(k1) #this is a list
    l2=str1[i]
    #l=[]
    for j in l1:
      l.append(l2+j)
  
  return l
  
print(permSt(str1))


# In[ ]:



