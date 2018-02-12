a=input("Enter the number of elements in an array:")
msg_array=list()
print("Enter the elements to be added:")
for i in range(int(a)):
    n=raw_input()
    msg_array.append(int(n))
for r in range(2,a):
 Total=sum(msg_array)
print(Total)
