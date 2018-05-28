a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
if a and b>0:
  temp=a
  a=b
  b=temp
print("The value of a after swaping is %d" %a)
print("The value of b after swaping is %d" %b)
