# -*- coding: utf-8 -*-
"""Task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11U1Jq-hfafCjyQcQYQmu9Lpy0s8OFYz9
"""



#Task-2

f1=open('/content/drive/MyDrive/CSE221_lab-04/Input2.txt',mode='r')
f2=open('/content/drive/MyDrive/CSE221_lab-04/Output2.txt',mode='w')
n1=f1.readline()
l=f1.readline().split( )
list1=[]
for num in l:
  list1.append(int(num))
def maxVal(arr):
  if len(arr) <= 1:
    return 
  else:
    mid = len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    maxVal(left)  
    maxVal(right) 
    # print(left,'l')
    # print(right,'r')
    l_max=max(left)
    r_max=max(right)
    # print(l_max,'l_max')
    # print(r_max,'r_max')
    ans=[l_max,r_max]
    return ans
ans=maxVal(list1)
a=max(ans)
print(str(a),file=f2)
f2.close()