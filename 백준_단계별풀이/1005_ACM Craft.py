'''
그냥 위상정렬 문제

모든 건물을 가장 빨리 지을 때까지 걸리는 시간
1. 먼저 설치해야하는 것들 중 heapq로 가장 가장 빨리 되는거 설치
2. 전체 시간을 카운트하면서 제일 빨리 건물이 지어지는게 끝나면 
-> 다음 지어질 수 있는거 체크

'''
import sys
from collections import deque
input = sys.stdin.readline

result = []
for _ in range(int(input())):
    n, k = map(int, input().split())
    each_buildtime = [0] + list(map(int, input().split()))
    
    # 건물 순서
    indegree = [0 for _ in range(n+1)] # indegree = [0] * (n+1) # 1 ~ n
    graph = [[] for _ in range(n+1)] # 1 ~ n
    for _ in range(1, k+1):
        first, last = map(int, input().split())
        graph[first].append(last)
        indegree[last] += 1
    target = int(input())

    # i를 짓는데까지 걸리는 시간
    time = [0 for _ in range(n+1)] # time = [0] * (n+1) 
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i) # (번호)
            time[i] = each_buildtime[i]

    # indegree == 0부터 탐색 시작
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            indegree[i] -= 1
            time[i] = max(time[i], time[now] + each_buildtime[i]) # time[i]까지 가려면 저정도 시간을 지나야한다.
            if indegree[i] == 0:
                q.append(i)
    result.append(time[target])
for i in result:
    print(i)