num=int(input("Enter an integer:"))
sum=0
while(num>0):
  rem=num%10
  sum=sum+rem
  num=num//10
if num==0:
  print("The sum of the integers is %d" %sum)
