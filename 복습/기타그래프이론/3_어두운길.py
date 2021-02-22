'''
제일 짧은길로 모든 도시 잇는다.
-> 크루스칼 O(ElogE) = 200백만 x log(200) = 충분

버려지는 금액 다 더하면됨.

'''
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

n, m = map(int, input().split())
edges = []
parent = [0] * (n+1)

# 부모 초기화
for i in range(1, n+1):
    parent[i] = i
# 도로상황 입력
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost,a,b))
edges.sort()

# 모든 도로 보자
total = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
    else:
        total += cost
print(total)
