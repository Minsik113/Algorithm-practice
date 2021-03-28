'''
마을 1~v
v:마을 수  E:도로 수
v = 400이라 플로이드안됨.
각도시들마다 다익스트라
O(VlogE) x V = 160000 * 80 = 천만안됨.

1. 도로정보 입력받는다.
2. 최단거리들을 구한다?
3. [a][b]와 [b][a]가 INF가 아닌애들끼리 최소값 비교

----
다른답보면 '플로이드워셜'로 풀어서 O(V^3)이므로 pypy3로 제출,,
1. 플로이드워셜이용
2. graph[i][i]로 오는 값이 있다면 있는애들끼리 최소값 비교
'''
##########################################
##########################################
# 3/28 - pypy3로는 됨.
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
distance = [[INF]*(v+1) for _ in range(v+1)] # i번도시에서 각도시까지의거리

# 1. 도로의 연결관계
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c= map(int, input().split())
    graph[a].append((b,c)) # a->b c

# 2. 모든도로 -> 모든도로 의 최단거리
def dijkstra(start):
    q = []
    distance[start][start] = 0 # 자기자신으로오는건 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[start][now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[start][i[0]] > cost:
                distance[start][i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

for i in range(1, v+1):
    dijkstra(i)

# 3. [a][b] 와 [b][a]가 있는애들만 체크
min_value = INF
for i in range(1, v+1):
    for j in range(i+1, v+1):
        # 사이클이 존재하면
        if distance[i][j] != INF and distance[j][i] != INF:
            min_value = min(min_value, distance[i][j] + distance[j][i])

if min_value == INF:
    print(-1)
else:
    print(min_value)