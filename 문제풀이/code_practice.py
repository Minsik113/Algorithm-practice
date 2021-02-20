INF = int(1e9)

n = int(input())
m = int(input())
# 인접행렬만들자
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기자신으로 오는 비용 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드워셜 진행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("INFINITY")
        else:
            print(graph[i][j])
    print()