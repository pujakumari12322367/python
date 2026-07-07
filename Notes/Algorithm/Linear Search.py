arr = [2,100,9,105,10,20,15,36,55,42]
key = 15
for i in range(len(arr)):
    if arr[i] == key:
        print("Element Found at", i)
        break
else:
    print("Element Not Found")