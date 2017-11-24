
# coding: utf-8

# Write a method that returns all subsets of a set.

# In[ ]:

l=[1,2,3]
def allSet(l):
  if(len(l)==1):
    return l
  
  a=len(l)
  a=a//2
  left=l[0:a]
  right=l[a:]
  a1=allSet(left)
  a2=allSet(right)
  k=[]
  k.extend(a1)
  k.extend(a2)
  for i in a1:
    for j in a2:
      temp=int(str(i)+str(j))
      k.append(temp)
  return k
      
    
    
kk=allSet(l)
kk.append('None')
print(kk)

