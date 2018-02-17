n=int(input("Enter the number of elements in an array:"))
Total=0
msg_array=list()
for i in range(0,n):
    n=raw_input()
    msg_array.append(int(n))
k=int(input("Enter the elements to be added:"))
if(n>k):
  for i in range(0,k):
    Total=Total+msg_array[i]
    print(Total)
else:
   print("not valid")
