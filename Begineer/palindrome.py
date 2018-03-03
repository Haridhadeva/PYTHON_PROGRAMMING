n=int(input("enter a value"))
temp=n
rev=0
while(n>0):
    perform=n%10
    rev=rev*10+perform
    n=n//10
if(temp==rev):
    print("the number is a palindrome")
else:
    print("the number is not a palindrome")
    
