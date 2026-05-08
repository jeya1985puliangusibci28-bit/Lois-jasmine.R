def print_twice_repeated(L):
    counts = {}
    for num in L:
        counts[num] = counts.get(num, 0) + 1
    
    
    printed = set()
    
    
    result = []
    for num in L:
        if counts[num] == 2 and num not in printed:
            result.append(str(num))
            printed.add(num)
    
    if result:
        print(" ".join(result))
# Example input handling
L = list(map(int, input().split()))
print_twice_repeated(L)
