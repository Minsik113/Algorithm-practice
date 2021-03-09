'''
start -> x번 도시로 이동
cost = 1초걸림

start -> k도시 -> x도시
=>다익스트라2번
or
플로이드로 graph[start][k] + graph[k][x]

'''
##########
# 플로이드워셜
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

# 1. 맵 초기화.(인접행렬 초기화)
graph = [[INF]*(n) for _ in range(n)]

# 2. 최단거리 초기화
for i in range(n): # 자기자신은 걸리는 거리 0으로 초기화
    graph[i][i] = 0

# 맵 입력받는다.
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

# 도착도시, 거치는도시 
end, rest = map(int, input().split())
rest -= 1
end -= 1

print(graph)
# 3. 탐색 시작
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
print(graph)
# 값이 있는지 없는지 체크
if graph[0][rest] == INF or graph[rest][end] == INF:
    print(-1)
else:
    print(graph[0][rest] + graph[rest][end])
