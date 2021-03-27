'''
n개의정수 중 x가 존재하는가?

1.이진탐색
n=10^5  nlogn = 2백만?
-> 정렬해서 이진탐색 m개
m(nlogn + logn)
O(MNlogN)?

2. dict에 넣고 있나 체크
N개를 넣고 M개를 다 봐야함
O(N + M)

3. set에 넣고 있나 체크
O(N + M) -> 제일빠르네?
'''
##########################################
##########################################
# 3. set()
import sys
input = sys.stdin.readline

n = int(input())
data = set(map(int, input().split()))
m = int(input())
array = list(map(int, input().split()))
for i in range(m):
    if array[i] in data:
        print(1)
    else:
        print(0)

##########################################
##########################################
# 2. dict()
# import sys
# input = sys.stdin.readline

# n = int(input())
# data = list(map(int, input().split()))
# m = int(input())
# array = list(map(int, input().split()))

# # dict에 넣자
# tree = dict()
# for i in range(n):
#     if str(data[i]) not in tree:
#         tree[str(data[i])] = 1
# # dict에 있나 보자
# for i in range(m)    :
#     if str(array[i]) in tree:
#         print(1)
#     else:
#         print(0)

##########################################
##########################################
# 1. 이진탐색
# from collections import deque
# import sys
# input = sys.stdin.readline

# n = int(input())
# data = list(map(int, input().split()))
# m = int(input())
# array = list(map(int, input().split()))

# data.sort()

# # data리스트안에 x값이 있는지 파악
# def check(data, x):
#     start = 0
#     end = len(data) - 1
#     flag = False
#     while start <= end:
#         mid = (start + end) // 2
#         # 중앙값이 찾고자 하는 값보다 작으면 범위 크게해서보자
#         if data[mid] == x:
#             flag = True
#             break
#         elif data[mid] < x:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return flag

# # array원소들이 data안에 있는지 파악하자
# for i in range(m):
#     # array[i]가 data안에 있다면
#     if check(data, array[i]):
#         print(1)
#     else:
#         print(0)

