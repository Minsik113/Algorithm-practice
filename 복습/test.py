array = [7,5,9,0,3,1,6,2,4,8] # 10개

length = len(array)

# 퀵정렬
def quick_sort(array, start, end):
    if start >= end: # 정렬해야할 원소가 1개면 종료
        return
    pivot = start # 첫번쨰 원소를 pivot으로 삼자
    left = start + 1
    right = end
    while (left <= start): # 지금 정한 pivot에 대해서 1cycle수행
        # 앞부터는 피벗보다 큰 데이터를 찾을 때까지 반복
        while (left <= end and array[left] <= array[pivot]):
            left += 1
        # 뒤부터는 피벗보다 작은 데이터를 찾을 때까지 반복
        while (right > start and array[right] >= array[pivot]):
            right += 1
        if (left > right): # 엇갈렸다면 작은데이터와 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[pivot] = array[pivot], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, length-1)
print(array)


# 삽입정렬 
# for i in range(1, length):
#     for j in range(i, 0, -1):
#         if array[j] < array[j-1]:
#             array[j], array[j-1] = array[j-1], array[j]
#         else:
#             break
# print(array)

# 선택정렬
# for i in range(length):
#     min_index = i
#     for j in range(i+1, length):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[min_index], array[i] = array[i], array[min_index] 
# print(array)