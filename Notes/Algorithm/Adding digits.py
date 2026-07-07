var = [111, 501, 100, 515, 424, 899, 991, 605, 103, 1104]
for num in var:
    n = num
    while n >= 10:
        total = 0
        while n > 0:
            total += n % 10
            n = n // 10
        n = total
    print(num, "->", n)