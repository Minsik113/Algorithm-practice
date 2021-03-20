##########################################
##########################################
# combination풀이
from itertools import combinations

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
array = [i for i in range(n)]
min_value = int(1e9)
total = set()

for left in combinations(array, n//2):
    right = set()
    right = []
    for i in range(n):
        if i not in left:
            right.append(i)
    # 봤던거 안보기 위해서
    if left in total:
        break
    total.add(left)
    total.add(tuple(right))
    
    left = list(left)
    right = list(right)
    # left, right 합구하자
    l_sum, r_sum = 0, 0
    for i in range(len(left)):
        for j in range(len(right)):
            l_sum += data[left[i]][left[j]]
            r_sum += data[right[i]][right[j]]
    # print(left, right, l_sum, r_sum)
    min_value = min(min_value, abs(l_sum - r_sum))
print(min_value)
##########################################
##########################################
# 백트래킹 은 왜케안풀림? 시간초과
# '''
# n = 짝수
# n명을 반띵해라.
# 1. a팀 n//2명 을뽑아라.
# 2. b팀은 나머지
# 3. a팀에 속한애들 a_sum 에두고 
# 4. a팀에 안속하면 b_sum에 더한다.
# 5. abs(a_sum - b_sum)이 제일 작은값을 구해라
# '''
# import sys
# input = sys.stdin.readline

# min_value = int(1e9)
# n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)]  # 번호 0~n-1
# left = []
# count = [1] * n
# # x가 left에 들어가도 되는가? 
# def check(x, depth):
    
#     # 넣을 수 있다.
#     if count[x] == 1: 
#         for i in range(depth): # depth아래로 x보다 큰 수가 나오면 불가
#             if left[i] > x:
#                 return False
#         # depth아래로 x보다 큰수가 없으므로 left에 추가
#         return True
#     # 넣을 수 없으면 False
#     return False

# def solve(depth):
#     global min_value
#     # left다 찼다. 합들구하면됨
#     if depth == n//2:
#         l_sum = 0
#         r_sum = 0
#         right = []
#         # right 구한다
#         for i in range(n):
#             if i not in left:
#                 right.append(i)
#         # 합들을 구해주자
#         for i in range(len(left)):
#             for j in range(n//2):
#                 if i == j:
#                     continue
#                 l_sum += data[left[i]][left[j]]
#                 r_sum += data[right[i]][right[j]]
#         # min값
#         min_value = min(min_value, abs(l_sum-r_sum))
#         print(left,right,l_sum,r_sum)
#         return
#     # 0~n번까지 수를 넣으면됨
#     for i in range(n):
        
#         if check(i, depth): # i넣어도됨?
#             count[i] -= 1
#             left.append(i)
#             solve(depth + 1)
#             count[i] += 1
#             left.pop()
        
# solve(0)
# print(min_value)