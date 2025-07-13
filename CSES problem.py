a=int(input())
list=[]
while a!=1 :
 if a % 2 == 0 :
  a=a/2
  list.append(a)
 else:
  a=a*3+1
  list.append(a)
print (list)  
