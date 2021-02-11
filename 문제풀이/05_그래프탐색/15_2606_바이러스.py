'''
# 1/29
# 문제 난이도:
# 출제 유형: DFS, BFS
# 추천 풀이 시간: 30분
'''
'''
컴퓨터 수가 적으므로 dfs로 빠르게 풀어도 유리함.
짧으니 재귀함수 limit에 안걸림.!
dfs쓰는이유는 코드가 짧음
'''
from collections import deque

n = int(input())
m = int(input())
array = [[] for i in range(n+1)] # 링크드리스트
visited = [False] * (n+1) # 노드당 방문했는지.
for i in range(m):
    a, b = map(int, input().split())
    array[a].append(b)
    array[b].append(a)

def bfs(v):
    visited[v] = True
    q = deque([v])
    count = 0
    while q:
        pos = q.popleft()
        for i in array[pos]:
            if not visited[i]: # 연결되어 있는데 아직안본애라면 추가
                q.append(i)
                visited[i] = True
                count += 1
    return count

count = 0

def dfs(v):
    global count
    visited[v] = True
    count += 1
    for next_pos in array[v]:
        if not visited[next_pos]:
            dfs(next_pos)
    
# print(bfs(1))
dfs(1)
print(count-1)