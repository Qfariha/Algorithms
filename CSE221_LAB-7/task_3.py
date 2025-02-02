# -*- coding: utf-8 -*-
"""Task-3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11U1Jq-hfafCjyQcQYQmu9Lpy0s8OFYz9
"""

#Task-3
import heapq as heapq

f1=open('/content/drive/MyDrive/CSE221_LAB-7/Input3.txt',mode='r')
f2=open('/content/drive/MyDrive/CSE221_LAB-7/Output3.txt',mode='w')
l1=f1.readline().split( )
n=int(l1[0])
e=int(l1[1])
d= {}
parent=[]
for i in range(n+1):
  parent.append(i)
#print(parent)
pq=[]
t_cost=0
e_cnt=0

for i in range(e):
  l2=f1.readline().split()
  u=int(l2[0])
  v=int(l2[1])
  w=int(l2[2])
  heapq.heappush(pq,(w,u,v))

#print(pq,'before')  
  
  
def find_parent(node):
  global parent
  return parent[node-1]
def union(s,des,cost):
  global t_cost
  
  if find_parent(s)!=find_parent(des):
    parent[des-1]=s
    t_cost+=cost
 
while e_cnt<n-1:
  cost,s,des=heapq.heappop(pq)
  #print(cost,'cost',s,'source',des,'des')
  
  union(s,des,cost)
  e_cnt+=1 



#print(pq)

#print(parent)
print(t_cost,file=f2)