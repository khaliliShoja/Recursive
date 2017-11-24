
# coding: utf-8

# Implement the “paint fill” function that one might see on many image editing programs. That is, given a screen (represented by a 2 dimensional array of Colors), a point, and a new color, fill in the surrounding area until you hit a border of that color.’

# In[2]:

N=[[1,1,1],[1,2,2],[1,2,3]]
l=[2,2]
k=1
a=N[l[0]][l[1]]
# a is the initial color
# l is point
#k is color
def paintFill(N,l,k,a):
  x=len(N[0])-1
  y=len(N)-1
  
  if (a!=N[l[0]][l[1]]):
    return
  else:
    N[l[0]][l[1]]=k
  
  if(l[0]<x):
    #print(l[0])
    l[0]=l[0]+1
    paintFill(N,l,k,a)
  if(l[0]>0):
    l[0]=l[0]-1
    paintFill(N,l,k,a)
  if(l[1]<y):
    l[1]=l[1]+1
    paintFill(N,l,k,a)
  if(l[1]>0):
    l[1]=l[1]-1
    paintFill(N,l,k,a)
    
  
print(N)
paintFill(N,l,k,a)
print(N)


# In[ ]:



