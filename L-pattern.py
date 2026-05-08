for row in range(6):
    for col in range(7):
        if col == 0 or row == 5:
            print("*", end="")
        else:
            print(" ", end="")
    print()
