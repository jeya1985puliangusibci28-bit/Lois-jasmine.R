
numbers = list(map(int, input("Enter 10 integers separated by space: ").split()))
MyList1 = []
MyList2 = []
for num in numbers:
    if num % 2 == 0 and num % 3 != 0:
        MyList1.append(num)
    if num % 9 == 0:
        MyList2.append(num)

print("MyList1:", MyList1)
