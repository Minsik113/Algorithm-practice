'''
n = 10^2
m = 10^5 

-> 모든 도시에서 모든도시까지의 거리구해라
O(N^3) = 10^6

'''
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())

# 1. 거리저장 할 인접행렬 선언
graph = [[INF] * (n+1) for _ in range(n+1)] # 1~n index까지

# 2. 맵 입력받는다.
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if graph[a][b] != INF: # 이미들어가있다면 작은값넣어라
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c

# 자기자신은 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# 1. 플로이드워셜 시작
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1): 
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 2. 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()