# n = int(input())
# data = list(map(int, input().split()))
# add, sub, mul, div = map(int, input().split())

# max_value = int(-1e9)
# min_value = int(1e9)

# # dfs
# def dfs(i, now):
#     global min_value, max_value, add, sub, mul, div
#     # 모든 연산자를 다 사용한 경우, 최솟값, 최대값 업데이트
#     if i == n:
#         min_value = min(min_value, now)
#         max_value = max(max_value, now)
#     else:
#         if add > 0:
#             add -= 1
#             dfs(i+1, now+data[i])
#             add += 1
#         if sub > 0:
#             sub -= 1
#             dfs(i+1, now-data[i])
#             sub += 1
#         if mul > 0:
#             mul -= 1
#             dfs(i+1, now*data[i])
#             mul += 1
#         if div > 0:
#             div -= 1
#             dfs(i+1, int(now/data[i]))
#             div += 1    
# dfs(1, data[0])
# print(max_value)
# print(min_value)
##########################################
##########################################
# 너무느림.
# from itertools import permutations

# n = int(input()) # 수의개수
# numbers = list(map(str, input().split()))
# oper_type = ['+', '-', '*', '/']
# oper_count = list(map(int, input().split()))

# # 사용할 수 있는 연산자 종류 체크
# operators = dict()
# for i in range(4):
#     operators[oper_type[i]] = oper_count[i]

# # operators로 n-1개의 모든경우 수 생성해라. 중복x = 순열
# row = [''] *(n-1)
# result = []
# def solve(depth):
#     if depth == n-1: # row에 연산자배열 
#         save = numbers[0]
#         for i in range(n-1):
#             save = eval(str(save) + row[i] + numbers[i+1])
#             save = int(save)
#         result.append(save)
#         return
#     for i in range(4): # 연산자 1개씩 넣어준다
#         row[depth] = oper_type[i]
#         if check(depth):
#             operators[row[depth]] -= 1
#             solve(depth+1)
#             operators[row[depth]] += 1
# def check(depth):
#     if operators[row[depth]] > 0:
#         return True
#     return False

# solve(0)
# print(result)

# print(max(result))
# print(min(result))
