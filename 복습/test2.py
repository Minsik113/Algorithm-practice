##########################################
##########################################
# 3/

##########################################
##########################################
#
'''
mst문제네.
=> 대각선의 개수 = n(n-3)/2 이므로 모든 거리를 구하면 10만^2가됨. 불가능
필요한것만 저장해야한다.

두행성의 비용구한다
edges = [비용,x,y] 식으로 저장
-> heapq이용해서 하나씩 pop하면서 보자

'''
import sys, heapq
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

# 부모 선언 및 초기화
parent = [0] * (n+1) # 1~n
for i in range(1, n+1):
    parent[i] = i

# 1번. 행성들의 좌표
x = []
y = []
z = []
for i in range(1, n+1):
    a, b, c = map(int, input().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))
x.sort()
y.sort()
z.sort()

# 2번. 별->별 까지의 거리.
edges = []
for i in range(n-1):
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))



# 3번. MST START 
result = 0
while h:
    cost, x, y = heapq.heappop(h)
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost
print(result)
