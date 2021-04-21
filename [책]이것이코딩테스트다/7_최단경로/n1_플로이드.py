##########################################
##########################################
# 4/21 - 
'''
자기자신으로 가는길 0으로 하는거 잊지말자
'''


##########################################
##########################################
# 3/21 복습 - 왜 주석처리한곳 틀렸다고 ? 같은말아닌가
'''
모든도시에서 모든도시로 가는 최단경로를 구해라.
이건 매번 다익스트라를 할 수 없으므로 플로이드가 적당해보인다.
-> 매번다익스트라를 할 수 없는이유 i와 j의 최단거리가 갱신될수있는지
매번 체크하기가 까다롭다. -> 3중포문으로 하는게 편할듯. 

다른 방법은 나중에한번 생각해보자.
Floyd
'''
import sys 
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
# 각 도시까지의 거리
distance = [[INF] * (n + 1) for _ in range(n+1)] 
for i in range(1, n+1):
    distance[i][i] = 0
# 도시의 연결관계
tree = dict()
for i in range(int(input())):
    a, b, cost = map(int, input().split())
    if distance[a][b] != INF:
        distance[a][b] = min(distance[a][b], cost)
    else:
        distance[a][b] = cost
    # cost = int(cost)
    # s = a+b
    # # 없으면 넣어주고
    # if s not in tree:
    #     tree[s] = cost
    #     distance[int(a)][int(b)] = cost
    # # 있으면 작은값으로 넣어줌
    # else:
    #     if cost < tree[s]:
    #         tree[s] = cost
    #         distance[int(a)][int(b)] = cost
# 플로이드 시작
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
# 
for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] == INF:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()
##########################################
##########################################
#
# '''
# n = 10^2
# m = 10^5 

# -> 모든 도시에서 모든도시까지의 거리구해라
# O(N^3) = 10^6

# '''
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n = int(input())

# # 1. 거리저장 할 인접행렬 선언
# graph = [[INF] * (n+1) for _ in range(n+1)] # 1~n index까지

# # 2. 맵 입력받는다.
# for _ in range(int(input())):
#     a, b, c = map(int, input().split())
#     if graph[a][b] != INF: # 이미들어가있다면 작은값넣어라
#         graph[a][b] = min(graph[a][b], c)
#     else:
#         graph[a][b] = c

# # 자기자신은 0으로 초기화
# for i in range(1, n+1):
#     graph[i][i] = 0

# # 1. 플로이드워셜 시작
# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1): 
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# # 2. 출력
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if graph[i][j] == INF:
#             print(0, end=' ')
#         else:
#             print(graph[i][j], end=' ')
#     print()
