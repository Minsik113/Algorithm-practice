'''
퀵 = pivot정해서 작으면왼쪽, 크면오른쪽
'''
array = [1,5,2,7,4,10,123,2,20593,0,6,8,9,14]

def quick_sort(array, start ,end):
    if start > end:
        return

    pivot = start 
    left = start+1
    right = end
    
    while left <= right:
        # 앞부터 피벗보다 큰 데이터 찾을때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 뒤부터 피벗보다 작은 데이터 찾을때까지 반복
        while right > start and array[right] > array[pivot]:
            right -= 1
        # 엇갈렸다면 작은 데이터와
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)