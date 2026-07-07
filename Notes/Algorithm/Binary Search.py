arr = [2,9,10,15,20,36,42,55,100,105]
key = 20
low = 0
high = len(arr)-1
while low <= high:
    mid = (low+high)//2
    if arr[mid] == key:
        print("Found")
        break
    elif arr[mid] < key:
        low = mid+1
    else:
        high = mid-1