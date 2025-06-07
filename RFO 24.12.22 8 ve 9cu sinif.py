s=input()
cem=1
l=[]
saitler='AEIOUY'
for i in s:
    if i not in saitler:
        cem=cem+1
    else: 
        l.append(cem)
        cem=1
l.sort()
print(l[-1])           