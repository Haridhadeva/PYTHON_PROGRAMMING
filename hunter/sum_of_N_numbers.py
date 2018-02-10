a=int(input("Enter the number:"))
if(a<1 or (a%1)!=0):
    print("wrong input")
else:
    temp=0
    while(a!=0):
        temp=temp+a
        a=a-1
    print (temp)
