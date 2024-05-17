# -*- coding: utf-8 -*-
"""Task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11U1Jq-hfafCjyQcQYQmu9Lpy0s8OFYz9
"""



#Task-3
f1=open('/content/drive/MyDrive/CSE221_Lab-02/Input3.txt',mode='r')
f2=open('/content/drive/MyDrive/CSE221_Lab-02/Output3.txt',mode='w')
n1=f1.readline()
list1=f1.readline().split( )
ans=[]
def mergeSort(arr):
  if len(arr) <= 1:
    return 
  else:
    mid = len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    mergeSort(left)  
    mergeSort(right)  
    merge(arr,left, right)

def merge(a,l,r):
  i=0
  j=0
  k=0
  while i<len(l) and j<len(r):
    if int(l[i])<int(r[j]):
      a[k]=int(l[i])
      i+=1
      k+=1
    else:
      a[k]=int(r[j])
      j+=1
      k+=1
  while i<len(l):
    a[k]=int(l[i])
    i+=1
    k+=1
  while j<len(r):
    a[k]=int(r[j])
    j+=1
    k+=1
  #print(a)
  
    
  
mergeSort(list1)
#print(list1,"l")
for num in list1:
  print(num,end=" ",file=f2)
  
f2.close()