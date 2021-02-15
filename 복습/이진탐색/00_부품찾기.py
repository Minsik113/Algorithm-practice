'''
n개의 부품 10^6
m개의 부품 10^5
n개의 부품에서 m개의 부품각각이 있는지 체크해야함.
-> 1. 이진탐색사용 -> n개의 부품받고 while로 m개 돌리면될듯?
-> 2. 계수정렬 -> N이 100만이니까.
-> 3. set()

N부품정렬 = O(NlogN) = 2000만
이진탐색 = O(MlogN) = 10^5 x 20 = 2백만. 가능
O((N+M)logN)
'''
##########################################
##########################################
# set사용
import sys
input = sys.stdin.readline
n = int(input())
n_array = set(map(int, input().split()))
m = int(input())
m_array = list(map(int, input().split()))

for i in m_array:
    if i in n_array:
        print('yes')
    else:
        print('no')

# ##########################################
# ##########################################
# # 계수정렬 사용
# import sys
# input = sys.stdin.readline
# n = int(input())
# checkbox = [0] * 1000001
# # 번호체크
# for i in input().split():
#     checkbox[int(i)] = 1

# m = int(input())
# m_array = list(map(int, input().split()))
# for i in m_array:
#     if checkbox[i] == 1:
#         print('yes')
#     else:
#         print('no')


##########################################
##########################################
# 함수 사용 (단순반복문사용)
# import sys
# input = sys.stdin.readline
# n = int(input())
# n_array = list(map(int, input().split()))
# m = int(input())
# m_array = list(map(int, input().split()))
# n_array.sort() # 10^6 x 20 = 2000만

# def binary_search_tree(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if n_array[mid] == target:
#             return mid
#         elif n_array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None

# for target in m_array:
#     result = binary_search_tree(n_array, target, 0, n-1)
#     if result != None: # 
#         print('yes')
#     else:
#         print('no')

##########################################
##########################################
# 함수안쓰고 반복문 사용
# import sys
# input = sys.stdin.readline
# n = int(input())
# n_array = list(map(int, input().split()))
# m = int(input())
# m_array = list(map(int, input().split()))
# n_array.sort() # 10^6 x 20 = 2000만

# for target in m_array: # n_array에서 target을 찾을것이다.
#     start = 0
#     end = n-1
#     check = False
#     while start <= end:
#         mid = (start + end) // 2
#         if n_array[mid] == target:
#             check = True
#             break
#         elif n_array[mid] > target: # 찾으려는게 더 작다->크기줄여
#             end = mid - 1
#         else:
#             start = mid + 1
#     if check: # True면 있음
#         print('yes')
#     else:
#         print('no')
