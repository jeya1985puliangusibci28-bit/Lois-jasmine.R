J=int(input("Enter the mark 1:"))
A=int(input("Enter the mark 2:"))
S=int(input("Enter the mark 3:"))
S=int(input("Enter the mark 4:"))
Total=J+A+S+S
print("The total mark is:",Total)
aggregate=Total/400*100
print("The percentage is:",aggregate)
if(aggregate>75):
    print("distribution")
elif(60<=aggregate>75):
    print("first division")
elif(50<=aggregate>60):
    print("second division")
elif(40<=aggregate>50):
    print("third division")
else:
    print("fail")
