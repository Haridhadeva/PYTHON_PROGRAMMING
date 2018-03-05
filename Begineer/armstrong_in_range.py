m=int(input("enter m value"))
n=int(input("enter n value"))
for i in range(m,n):
    s=0
    temp=i
    while i>0:
            a=i%10
            i=i//10
            s=a*a*a+s
    if s==temp:
            print("{0} is a armstrong number".format(temp))
    else:
            print("{0} is not a armstrong number".format(temp))
