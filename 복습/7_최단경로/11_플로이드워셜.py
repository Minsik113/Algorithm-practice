'''
모든노드 -> 모든 노드의 최단 경로를 모두 계산
2차원 테이블에 최단 거리 정보를 저장한다.
(DP유형에 속한다)
-> 점화식에 맞게 3중반복문을 이용하여 2차원 테이블을 갱신한다.

O(N^3) 500개아래로 보통 주어줌. 
: 각 단계마다 O(N^2)의 연산. -> 3중반복문
-> 즉, 노드의 개수가 적은 상황에서 효과적이며, 일반적으로 dijkstra사용

Dab = min(Dab, Dak + Dkb)
-> a~>b의 최단거리는 min(a~>b, a~>k~>b)

-----방법-----
1/ 자기자신 -> 자기자신
2/ i행 i열
1,2번빼고 나머지 위치에 대한 테이블정보를 갱신해주면됨.

55분20초 https://www.youtube.com/watch?v=acqm9mM1P6o&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=7
'''
INF = int(1e9)

n = int(input())
m = int(input())
# 2차원 인접행렬 만들고, 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기자신으로 오는 비용 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A->B로 가는 비용 = C
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 실행
for k in range(1, n+1):
    for a in range(1, n+1): # a->b 로가는데 k를 거치는거
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[i][j], end=' ')
    print()


