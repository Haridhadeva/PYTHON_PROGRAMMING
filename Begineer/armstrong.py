n=int(input("enter a value"))
s=0
temp=n
while n>0:
    a=n%10
    n=n//10
    s=a*a*a+s
if s==temp:
    print("armstrong number")
else:
    print("not armstrong number")
