##########################################
##########################################
# 3/4 복습
'''
조건: O(logN)으로 해결해라
정렬된 배열이니까 이진탐색하자
'''
n = int(input())
array = list(map(int, input().split()))

start = 0 # 시작 인덱스
end = n-1

flag = False
while start <= end:
    mid = (start + end) // 2 # 중간 인덱스
    if mid == array[mid]:
        print(mid)
        flag = True
        break
    elif mid < array[mid]: # 찾은곳에 큰 값이있으면 더 작은곳을 봐야함
        end = mid -1
    else:
        start = mid + 1

if not flag:
    print(-1)
##########################################    
##########################################
#
'''
1. n개 10^6
2. n개에서 고정점이 있는지 찾자. O(logN)으로 구현해라.
-> 이진탐색하라는 이야기.
'''
n = int(input())
array = list(map(int, input().split()))

# 함수이용 - 단순반복문
# def binary_search_tree(array, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == mid:
#             return mid
#         elif array[mid] > mid: # 인덱스보다 값이 더크다면 왼쪽을봐야함
#             end = mid - 1
#         else:
#             start = mid + 1
#     return -1

# 함수이용 - 재귀
def binary_search_tree(array, start, end):
    if start > end:
        # return -1   # 재귀함수는 -1로 리턴해도 none으로나옴
        return None 
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid: # 나온값이 index보다 크니까 end줄여서 left보자
        return binary_search_tree(array, start, mid - 1) 
    else:
        return binary_search_tree(array, mid + 1, end) 


result = binary_search_tree(array, 0, n-1)
if result == None:
    print(-1)
else:
    print(result)


