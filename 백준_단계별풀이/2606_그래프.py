'''
2025.05.3 12:20~12:35
https://www.acmicpc.net/problem/2606

1번에 바이러스가 걸렸을때 바이러스가 걸린 총 컴퓨터 수는?
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    cnt = 0
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        x = q.popleft()
        for i in arr[x]:
            if not visited[i]:
                cnt += 1
                q.append(i)
                visited[i] = True
    
    return cnt

n = int(input())
m = int(input())
visited = [False]*(n+1)
arr = [[] for _ in range(n+1)] # 1~n
for _ in range(m):
    a,b = list(map(int,input().split()))
    arr[a].append(b)
    arr[b].append(a)

result = bfs(1)
print(result)