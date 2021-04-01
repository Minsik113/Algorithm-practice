##########################################
##########################################
# 3/28 - 아래코드보단 좀 빠름
import sys
input = sys.stdin.readline

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

n = int(input())
m = int(input())

# 부모 선언 및 초기화
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

for i in range(n): 
    array = list(map(int, input().split()))
    for j in range(n):
        if array[j] == 1:
            union_parent(parent, i+1, j+1) # 1~n+1

gocity = list(map(int, input().split()))

pre = find_parent(parent, gocity[0])
flag = True
for i in range(1, len(gocity)): # 1,2,3
    if find_parent(parent, gocity[i]) != pre:
        flag = False   
        break
print("YES" if flag else "NO")

##########################################
##########################################
# 3/28 - 첫 풀이
# '''
# union-find로 같은애들 묶어주면됨
# '''
# import sys
# input = sys.stdin.readline

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# n = int(input())
# m = int(input())
# array = [list(map(int, input().split())) for _ in range(n)]
# gocity = list(map(int, input().split()))

# # 부모 선언 및 초기화
# parent = [0] * (n+1)
# for i in range(1, n+1):
#     parent[i] = i

# for i in range(n): 
#     for j in range(n):
#         if array[i][j] == 1: # 0~n-1
#             union_parent(parent, i+1, j+1) # 1~n+1

# pre = gocity[0]
# flag = True
# for i in range(1, len(gocity)): # 1,2,3
#     if find_parent(parent, gocity[i-1]) != find_parent(parent, gocity[i]):
#         flag = False   
#         break
#     pre = gocity[i]
# print("YES" if flag else "NO")

