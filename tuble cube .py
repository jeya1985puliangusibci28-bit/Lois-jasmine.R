numbers = [1,2,3,4,5]
element = tuple(x**2 if x % 2 == 0 else x**3 for x in numbers)
print(element)
