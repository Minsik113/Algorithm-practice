'''
1. n,m입력.
n = 0~n이므로 n+1

'''
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def check(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        s = "Yes"
        return s
    else:
        s = "NO"
        return s

n, m = map(int, input().split())
parent = [0] * (n + 1) # 0~n
result = []
# 부모초기화
for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 1: # 같은팀인지 여부확인
        result.append(check(parent, a, b))
    else:
        union_parent(parent, a, b)

for i in result:
    print(i)

