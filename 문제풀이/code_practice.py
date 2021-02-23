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

n = int(input())

# 부모초기화
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

x = []
y = []
z = []
for i in range(n):
    a, b, c = map(int, input().split())
    x.append((a,i)) # 길이, 행성번호
    y.append((b,i))
    z.append((c,i))
x.sort()
y.sort()
z.sort()

# 짧은 행성부터 거리재서 edges에 넣는다
edges = []
for i in range(n-1): # AB거리,A,B
    edges.append(( x[i+1][0]-x[i][0], x[i+1][1], x[i][1]))
    edges.append(( y[i+1][0]-y[i][0], y[i+1][1], y[i][1]))
    edges.append(( z[i+1][0]-z[i][0], z[i+1][1], z[i][1]))

edges.sort()
# 짧은행성부터 union
total = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total += cost
print(total)
