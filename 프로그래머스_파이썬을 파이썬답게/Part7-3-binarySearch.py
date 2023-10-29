def binarySearch(a, x):
    end = len(a)
    start = 0
    while start < end:
        mid = (start + end) // 2
        if a[mid] < x:
            start = mid + 1
        else:
            end = mid
    return start

mylist = [1,2,3,7,9,11,33]
print(binarySearch(mylist, 3)) # return 2 즉, mylistp[2]에 위치