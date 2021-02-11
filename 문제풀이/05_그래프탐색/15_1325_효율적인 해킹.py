'''
# 1/29
# 문제 난이도: Silver 2
# 출제 유형: DFS, BFS
# 추천 풀이 시간: 30분
'''
'''
모든 정점에 대해서 dfs bfs를 수행한다.
방문하게 되는 노드 수 저장.
'''

from collections import deque

n, m = map(int, input().split()) # 컴퓨터개수, 관계수
array = [[] for i in range(n+1)] # 1번~5번컴퓨터에 연결된 애들
 # b를 신뢰하는 a들을 보자
 # b를 해킹하면 연결된 a들도 저절로 해킹됨.
for i in range(m):
    a, b = map(int, input().split()) # 1번~n번 컴퓨터
    array[b].append(a) 

def bfs(i):
    visited = [False] * (n+1)
    visited[i] = True
    q = deque()
    q.append(i)
    count = 1

    while q:
        x = q.popleft() # 1
        for k in array[x]: # 3
            if not visited[k]:
                visited[k] = True
                q.append(k)
                count += 1
    return count

 # 각 정점마다 몇개씩 연결되어 있는가.
result = [0] * (n+1)
for i in range(1,n+1):
    result[i] = bfs(i)
 # print(result)

maxnum = max(result)
for i in range(1,n+1):
    if result[i] == maxnum:
        print(i, end=' ')
