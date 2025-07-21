def is_leap(n):
 y=False
 if year % 4==0 and year%100!=0 :
     y=True
 elif year%100==0 and year%400==0:
     y=True
 return y 
year = int(input())
print(is_leap(year))