for i in range(5):
    for j in range(5):
        if (i == j) or (i + j == 4) or ((i == 1 or i == 3) and (j == 0 or j == 4)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()