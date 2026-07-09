var = [7, 3, 5, 9, 2, 12]

for i in range(1, len(var)):
    key = var[i]
    j = i - 1

    while j >= 0 and var[j] > key:
        var[j + 1] = var[j]
        j -= 1

    var[j + 1] = key

print("Sorted List:", var)