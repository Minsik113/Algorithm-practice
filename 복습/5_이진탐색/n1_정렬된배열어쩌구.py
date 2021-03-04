##########################################
##########################################
# 3/4 복습 bisect사용
from bisect import bisect_left, bisect_right

def search(data, m):
    left_index = bisect_left(data, m)
    right_index = bisect_right(data, m)
    return right_index - left_index

n, m = map(int, input().split())
data = list(map(int, input().split()))
result = search(data,m)
if result == 0: # 값이 없음
    print(-1)
else:
    print(result)
##########################################
##########################################
# 3/4 복습 이진탐색 구현
# m을 찾았을때 제일작은 index 찾는함수
# m을 찾았을때 제일작은 index 찾는함수
def front(data, taget):
    start = 0
    end = len(data) -1
    save_index = -1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] >= taget: # 찾은값이 target보다 크거나 같으면 작게해봄
            save_index = mid
            end = mid - 1
        else:
            start = mid + 1
    return save_index

# m을 찾았을때 제일큰 index 찾는함수
def last(data, taget):
    start = 0
    end = len(data) -1
    save_index = -1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] >= taget: # 찾은값이 target보다 크거나 같으면 최대한 작은값 찾기위해 움직임
            save_index = mid
            end = mid - 1
        else:
            start = mid + 1
    return save_index

# front_index와 last_index찾는 함수
def dif(data, m):
    a = front(data, m)
    # 예외처리 (값이 존재하지 않는다.)
    if a == -1: 
        return -1
    b = last(data, m+1)
    if a == b: # 값없음
        return -1
    return b - a

n, m = map(int, input().split())
data = list(map(int, input().split()))

result = dif(data, m)
print(result)
##########################################
##########################################
#
'''
이진탐색으로 해당 값의 index값찾는다.
그 후 해당index에서 앞뒤로 1씩 증감해보면서 같은 수인지 체크한다.

★★재귀함수는 -1로 리턴해도 None으로나옴★★
'''
# n, x = map(int, input().split())
# array = list(map(int, input().split()))
# # x의 시작index찾자
# low_index = 0
# high_index = 0

# def low_binary_search_tree(array, target, start, end):
#     global low_index

#     while start <= end:
#         mid = (start + end) // 2

#         if array[mid] == target:  # 1~2인곳을 찾아야함. 
#             if mid-1 >= 0: # 범위안에 존재하면 mid-1이 target과같은지확인. 아니라면 이게 최소값
#                 if array[mid-1] != target:
#                     return mid
#                 else: # 더작은위치를 보게 end줄인다
#                     end = mid - 1
#             else: # 이전값이 없으면 이게 제일작은 index지
#                 return mid
#         elif array[mid] > target: # 찾고자하는 수보다 크니까 줄여야함
#             end = mid - 1
#         else: 
#             start = mid + 1
#     return -1

# def high_binary_search_tree(array, target, start, end):
#     global high_index

#     while start <= end:
#         mid = (start + end) // 2

#         if array[mid] == target:  # 2~3인곳을 찾아야함. 
#             if mid+1 < n: # 범위안에 존재하면 mid-1이 target과같은지확인.
#                 if array[mid+1] != target:
#                     return mid
#                 else: # 더작은위치를 보게 end줄인다
#                     start = mid + 1
#             else: # 이후값이 없으면 이게 제일 큰 index지
#                 return mid
#         elif array[mid] > target: # 찾고자하는 수보다 크니까 줄여야함
#             end = mid - 1
#         else: 
#             start = mid + 1
#     return -1

# l = low_binary_search_tree(array, x, 0, n-1) # 시작인덱스~끝인덱스
# h = high_binary_search_tree(array, x, 0, n-1) # 시작인덱스~끝인덱스
# if l == -1:
#     print(-1)
# else:
#     print(h, l)
#     print(h - l + 1)

# ##########################################
# ##########################################
# # 같은수의 시작index와 마지막index를 찾아라. (둘다 이진탐색으로)
# n, x = map(int, input().split())
# array = list(map(int, input().split()))

# # 몇개나 있는지 확인하는 함수. 이곳에서 '중복된 x값의 처음index와 마지막index값'을 찾을것이다.
# def count_function(array, x, n):
#     first = find_first(array, x, 0, n-1)
#     if first == None: # 값이 존재하지 않는다면
#         return -1
#     last = find_last(array, x, 0, n-1)
#     print(last)
#     print(first)
#     return last - first + 1

# def find_first(array, x, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
    
#     # 해당 값을 가지는 원소중에서 가장 왼쪽에 있는 경우
#     if (mid == 0 or x > array[mid-1]) and array[mid] == x:
#         return mid
#     elif array[mid] >= x: # 찾고자하는게 작으면 end를 줄인다
#         return find_first(array, x, start, mid-1)
#     else:
#         return find_first(array, x, mid+1, end)
# def find_last(array, x, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
    
#     # 해당 값을 가지는 원소중에서 가장 왼쪽에 있는 경우
#     if (mid == n-1 or x < array[mid+1]) and array[mid] == x:
#         return mid
#     elif array[mid] > x: # 찾고자하는게 작으면 end를 줄인다
#         return find_last(array, x, start, mid-1)
#     else:
#         return find_last(array, x, mid+1, end)

# count = count_function(array, x, n)
# print(count)

