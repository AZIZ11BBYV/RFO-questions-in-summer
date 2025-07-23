n=input("Please, enter the input: ")
a=n.upper()
siyahi=[]
s=1 
for i in range (1,len(a)):
 if a[i-1]==a[i]:
  s+=1
 else:
  siyahi.append(s)
  s=1
siyahi.sort()
print(siyahi[-1])N
    
