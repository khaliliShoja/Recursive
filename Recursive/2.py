
# coding: utf-8

# Question:
# Imagine a robot sitting in the upper left hand corner of a NxN grid. The robot can only move in two directions: right and down. How many possible paths are there for the robot to reach to the lower right hand corner of the grid? Please show all the routes.
# 
# 
# In my solution, "D" stands for down and "R" stands for right.

# In[6]:

n=3
l=[]
def pathfinder(l, n, i, j):
  
  if(len(l)== 2*n-2):
    print(l)
    
  if(i < n-1):
    a=l[:]
    a.append('R')
    pathfinder(a, n , i+1, j)
  if(j < n-1):
    a=l[:]
    a.append('D')
    pathfinder(a,n,i,j+1)
  



pathfinder(l,n,0,0)


# In[9]:

n=2
l=[]
def pathfinder(l, n, i, j):
  if(len(l)== 2*n-2):
    return l
  if(i < n-1):
    a=l[:]
    a.append('R')
    l=pathfinder(a, n , i+1, j)
  if(j < n-1):
    a=l[:]
    a.append('D')
    l=pathfinder(a,n,i,j+1)
  return l


l=pathfinder(l,n,0,0)
print(l)
print("Number of paths is: ", int(len(l)/n))


# In[ ]:



