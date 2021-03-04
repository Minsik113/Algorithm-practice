'''
퀵정렬 O(N^2) O(NlogN)
pivot정해서 작으면왼쪽, 크면오른쪽
너비 x 높이 = N x logN = NlogN
최악의 경우 O(N^2)이다. (이미 정렬된 배열의 경우)

표준라이브러리는 항상 O(NlogN)이 되게 설계되어 있다.
-> 피벗위치를 맨앞부터 안보고 중간값찾기 했던것처럼 해서 그렇겠지?
'''
# 퀵정렬 최악O(N^2) 평균O(NlogN)

# 파이썬스러운 코드
array = [1,5,2,7,4,10,123,2,20593,0,6,8,9,14]

def quick_sort(array):
    # 리스트 길이 1이면 종료
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot] # 작으면 left_side
    right_side = [x for x in tail if x > pivot] # 크면 right_side

    # 분할이후
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
print(quick_sort(array))

# 일반적코드
# def quick_sort(array, start, end):
#     if start >= end: # 정렬해야할 원소가 1개면 종료
#         return
#     pivot = start # 첫번쨰 원소를 pivot으로 삼자
#     left = start + 1
#     right = end
#     while (left <= start): # 지금 정한 pivot에 대해서 1cycle수행
#         # 앞부터는 피벗보다 큰 데이터를 찾을 때까지 반복
#         while (left <= end and array[left] <= array[pivot]):
#             left += 1
#         # 뒤부터는 피벗보다 작은 데이터를 찾을 때까지 반복
#         while (right > start and array[right] >= array[pivot]):
#             right += 1
#         if (left > right): # 엇갈렸다면 작은데이터와 피벗 교체
#             array[right], array[pivot] = array[pivot], array[right]
#         else:
#             array[left], array[pivot] = array[pivot], array[left]
#     quick_sort(array, start, right-1)
#     quick_sort(array, right+1, end)

# quick_sort(array, 0, length-1)
# print(array)
