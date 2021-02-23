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

v, e = map(int, input().split())
parent = [0] * (v+1)

# 부모초기화
for i in range(1,v+1):
    parent[i] = i

# 모든 간선을 담을 리스트, 최종 비용 담을 변수
edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost,a,b)) 

edges.sort() # cost를 우선적으로 오름차순으로 정렬해준다.

for edge in edges:
    cost, a, b = edge
    # 사이클 발생안하면 추가시킴
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)