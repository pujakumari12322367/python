def search(var, element):
    var.sort()
    low = 0
    high = len(var) - 1
    while low <= high:
        mid_index = (low + high) // 2
        if var[mid_index] == element:
            print("Element Found at index", mid_index)
            return
        elif var[mid_index] < element:
            low = mid_index + 1
        else:
            high = mid_index - 1
    print("Element Not Found")
arr = [2, 100, 9, 105, 10, 20, 15, 36, 55, 42]
search(arr, 36)