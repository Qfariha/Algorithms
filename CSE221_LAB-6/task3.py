# -*- coding: utf-8 -*-
"""Task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11U1Jq-hfafCjyQcQYQmu9Lpy0s8OFYz9
"""



#Task-3
f1=open('/content/drive/MyDrive/CSE221_Lab-6/Input3.txt',mode='r')
f2=open('/content/drive/MyDrive/CSE221_Lab-6/Output3.txt',mode='w')
l1=f1.readline().split( )
n=int(l1[0])
e=int(l1[1])
d= {}
   
for i in range(e):
  
  l2=f1.readline().split()
  u=int(l2[0])
  v=int(l2[1])
  w=int(l2[2])
  
  for i in range(n+1):
    if i not in d:
      d[i]=[]

  if(u in d):
    d[u].append([v,w])

  elif u not in d:
    d[u] = [v,w]
print(d)   
def min_danger_level(adj_list, n):
  s = [(1, [1], 0)]  #stack with vertice, path_list,cost  
  min_cost = float('inf')
  min_path = None
  while s:
    vertice, path_list, cost = s.pop() #LIFO
    if vertice == n:  #destination vertice
      if cost < min_cost:
        min_cost = cost
        min_path = path_list
    else:
      for neighbor, edge_cost in adj_list[vertice]:
        if neighbor not in path_list:
          new_cost = max(cost, edge_cost)
          new_path_list = path_list + [neighbor]
          s.append((neighbor, new_path_list, new_cost))
  return min_cost
a=min_danger_level(d, n)
print(a,file=f2)
f2.close()