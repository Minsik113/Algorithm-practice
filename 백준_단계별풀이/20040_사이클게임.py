'''
평면에 0~n-1
세점을 일직선 위에 두지 않는다.

3점이 사이클이 생기는순간 종료
'''
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

# MAIN
n, m = map(int, input().split())
cycle = False # 사이클O -> True

# 부모 선언 및 초기화
parent = [0] * (n)
for i in range(n):
    parent[i] = i

# 탐색 시작
result = 0
for i in range(1, m+1):
    x, y = map(int, input().split())
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
    else:
        cycle = True
        if result == 0: # 한번만 저장할것이니까
            result = i
        
if cycle:
    print(result)
else:
    print(0)