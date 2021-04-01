##########################################
##########################################
# 4/1 - 간단함.
'''
0 a b = a가 속한 집합 + b가 속한 집합
1 a b = a와 b가 같은집합인가
'''
import sys
sys.setrecursionlimit(10**7)
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

n, m = map(int, input().split())
# 1. 부모 선언 및 초기화
parent = [0] * (n+1) # 0~n
for i in range(n+1):
    parent[i] = i
for _ in range(m):
    t, x, y = map(int, input().split())
    
    x = find_parent(parent, x)
    y = find_parent(parent, y) 
    
    # 합집합
    if t == 0:
        if x != y:
            union_parent(parent, x, y)

    # 출력
    else:
        if x != y:
            print("NO")
        else:
            print("YES")

    
