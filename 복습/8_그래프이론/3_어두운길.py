##########################################
##########################################
# 3/23복습 - 간선정렬로 heapq사용 minheap이라 O(nlogn)크기임
'''
제일 짧은 길로만 연결해라.

mst 사용해서 연결해라. 
전체 - 연결할때 드는 비용
'''
import heapq, sys
input = sys.stdin.readline

n, m = map(int, input().split())
# edges에 넣자
h = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    heapq.heappush(h, (cost, a, b))
# 부모 선언 및 초기화
parent = [0] * (n)
for i in range(n):
    parent[i] = i

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

total = 0 # 모든길
min_value = 0 #
while h:
    cost, a, b = heapq.heappop(h)
    total += cost
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        min_value += cost
print(total - min_value)

##########################################
##########################################
# # 간선정렬로 sort()이용- O(nlogn)
# '''
# 제일 짧은길로 모든 도시 잇는다.
# -> 크루스칼 O(ElogE) = 200백만 x log(200) = 충분

# 버려지는 금액 다 더하면됨.
# '''
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# n, m = map(int, input().split())
# edges = []
# parent = [0] * (n+1)

# # 부모 초기화
# for i in range(1, n+1):
#     parent[i] = i
# # 도로상황 입력
# for _ in range(m):
#     a, b, cost = map(int, input().split())
#     edges.append((cost,a,b))
# edges.sort()

# # 모든 도로 보자
# total = 0
# for edge in edges:
#     cost, a, b = edge
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#     else:
#         total += cost
# print(total)
