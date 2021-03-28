'''
모든도시 -> 모든도시로 가는 최소비용

플로이드 워셜

1. a->b로 가는 가장작은 길을 저장
'''
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

# 최단거리 저장할 리스트 선언 및 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    graph[i][i] = 0

# 길 입력받는다. 최소거리를 저장한다.
tree = dict()
for _ in range(m):
    a, b, c = map(int, input().split())
    # 이미 길이 존재하면 작은값으로 대체
    if graph[a][b] != INF:
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c

# 플로이드워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
# 출력            
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] != INF:
            print(graph[i][j], end=' ')
        else:
            print(0, end=' ')
    print()