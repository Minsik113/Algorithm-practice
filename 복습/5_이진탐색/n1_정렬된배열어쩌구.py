'''
이진탐색으로 해당 값의 index값찾는다.
그 후 해당index에서 앞뒤로 1씩 증감해보면서 같은 수인지 체크한다.

★★재귀함수는 -1로 리턴해도 None으로나옴★★
'''

n, x = map(int, input().split())
array = list(map(int, input().split()))
# x의 시작index찾자
low_index = 0
high_index = 0

def low_binary_search_tree(array, target, start, end):
    global low_index

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:  # 1~2인곳을 찾아야함. 
            if mid-1 >= 0: # 범위안에 존재하면 mid-1이 target과같은지확인. 아니라면 이게 최소값
                if array[mid-1] != target:
                    return mid
                else: # 더작은위치를 보게 end줄인다
                    end = mid - 1
            else: # 이전값이 없으면 이게 제일작은 index지
                return mid
        elif array[mid] > target: # 찾고자하는 수보다 크니까 줄여야함
            end = mid - 1
        else: 
            start = mid + 1
    return -1

def high_binary_search_tree(array, target, start, end):
    global high_index

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:  # 2~3인곳을 찾아야함. 
            if mid+1 < n: # 범위안에 존재하면 mid-1이 target과같은지확인.
                if array[mid+1] != target:
                    return mid
                else: # 더작은위치를 보게 end줄인다
                    start = mid + 1
            else: # 이후값이 없으면 이게 제일 큰 index지
                return mid
        elif array[mid] > target: # 찾고자하는 수보다 크니까 줄여야함
            end = mid - 1
        else: 
            start = mid + 1
    return -1

l = low_binary_search_tree(array, x, 0, n-1) # 시작인덱스~끝인덱스
h = high_binary_search_tree(array, x, 0, n-1) # 시작인덱스~끝인덱스
if l == -1:
    print(-1)
else:
    print(h, l)
    print(h - l + 1)

##########################################
##########################################
# 같은수의 시작index와 마지막index를 찾아라. (둘다 이진탐색으로)
n, x = map(int, input().split())
array = list(map(int, input().split()))

# 몇개나 있는지 확인하는 함수. 이곳에서 '중복된 x값의 처음index와 마지막index값'을 찾을것이다.
def count_function(array, x, n):
    first = find_first(array, x, 0, n-1)
    if first == None: # 값이 존재하지 않는다면
        return -1
    last = find_last(array, x, 0, n-1)
    print(last)
    print(first)
    return last - first + 1

def find_first(array, x, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    # 해당 값을 가지는 원소중에서 가장 왼쪽에 있는 경우
    if (mid == 0 or x > array[mid-1]) and array[mid] == x:
        return mid
    elif array[mid] >= x: # 찾고자하는게 작으면 end를 줄인다
        return find_first(array, x, start, mid-1)
    else:
        return find_first(array, x, mid+1, end)
def find_last(array, x, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    # 해당 값을 가지는 원소중에서 가장 왼쪽에 있는 경우
    if (mid == n-1 or x < array[mid+1]) and array[mid] == x:
        return mid
    elif array[mid] > x: # 찾고자하는게 작으면 end를 줄인다
        return find_last(array, x, start, mid-1)
    else:
        return find_last(array, x, mid+1, end)

count = count_function(array, x, n)
print(count)

##########################################
##########################################
# 내풀이. -> 같은수가 너무많으면 못쓴다.
# n, x = map(int, input().split())
# array = list(map(int, input().split()))

# def binary_search_tree(array, x, start, end):
#     count = 1
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == x:
#             # 이제 앞뒤로 개수 체크해보자.
#             save = mid
#             while mid-1 >= 0: # 이전 인덱스가 존재한다면
#                 if array[mid-1] == x:
#                     count += 1
#                     mid -= 1
#                 else:
#                     break
#             mid = save
#             while mid+1 <= end: # 이후 인덱스가 존재한다면
#                 if array[mid+1] == x:
#                     count += 1
#                     mid += 1
#                 else:
#                     break
#             return count
#         elif array[mid] > x: # 찾고자하는값이 더 작으면 end를 줄여야지
#             end = mid - 1
#         else:
#             start = mid + 1
    
#     return -1
    
# result = binary_search_tree(array, x, 0, n-1) # sortlist, target_value, start_index, end_index
# print(result)
    