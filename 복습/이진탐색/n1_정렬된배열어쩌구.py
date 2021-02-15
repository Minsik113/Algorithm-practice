'''
이진탐색으로 해당 값의 index값찾는다.
그 후 해당index에서 앞뒤로 1씩 증감해보면서 같은 수인지 체크한다.

★★재귀함수는 -1로 리턴해도 None으로나옴★★
'''

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
    