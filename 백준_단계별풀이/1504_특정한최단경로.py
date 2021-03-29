'''
1 -> v1 -> v2 -> n
1 -> v2 -> v1 -> n
둘중 짧은 거리를 출력한다.
다익스트라 3번쓰면됨

'''
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())

# 1. 연결관계 입력
graph = [[] for _ in range(n+1)]
for _ in range(e): # 무방향
    a, b, c = map(int, input().split())
    graph[a].append((b,c)) # 노드, cost
    graph[b].append((a,c))

v1, v2 = map(int, input().split())
# 거리
def dijkstra(start, x):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distance[x]

# 시작->v1->v2->끝
result = [1, v1, v2,n]
min_value1 = 0    
flag1 = True
pre = result[0]
for k in range(1, len(result)):
    distance = [INF] * (n+1)
    temp = dijkstra(pre, result[k])
    if temp != INF:
        min_value1 += temp
    else:
        flag1 = False
        break
    pre = result[k]
    
# 시작->v2->v1->끝
result = [1,v2,v1,n]
min_value2 = 0
flag2 = True
pre = result[0]
for k in range(1, len(result)):
    distance = [INF] * (n+1)
    temp = dijkstra(pre, result[k])
    if temp != INF:
        min_value2 += temp
    else:
        flag2 = False
        break
    pre = result[k]

# 예외처리. 간선정보가 없는경우엔 -1
if e == 0:
    print(-1)
    exit()
# 둘다 참이면 더 작은애 출력
if flag1 and flag2:
    print(min(min_value1, min_value2))
elif not flag1 and flag2:
    print(min_value2)
elif flag1 and not flag2:
    print(min_value1)
else:
    print(-1)

