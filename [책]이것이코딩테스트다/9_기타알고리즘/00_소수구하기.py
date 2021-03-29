'''
left ~ right 범위안의 소수구하기

에라토스테네스의 체 사용하자
O(NloglogN)
'''
##########################################
##########################################
#
import math

left, right = map(int, input().split())

check = [True] * 1_000_001 # 1~right
check[1] = False # 0은 어차피 안봄.

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(right))+1):
    if check[i]: # 안본애들중 제일 작은애라면 배수들 False로바꿈
        j = 2
        while (i*j) <= right:
            check[i*j] = False
            j += 1

for i in range(left, right+1):
    if check[i]:
        print(i)
##########################################
##########################################
# 내풀이
# import math

# left, right = map(int, input().split())
# right = right + 1

# check = [True] * (right+1) # 1~right
# check[1] = False # 0은 어차피 안봄.

# # 에라토스테네스의 체
# for i in range(2, int(math.sqrt(right))+1):
#     if check[i]: # 안본애들중 제일 작은애라면 배수들 False로바꿈
#         j = 2
#         while (i*j) <= (right):
#             check[i*j] = False
#             j += 1

# for i in range(left, right):
#     if check[i]:
#         print(i)


