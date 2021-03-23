'''
확실하게 순서를 정할 수 있
'''
from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input()) # 전체 팀 개수
    # 작년 등수
    indegree = [0] * (n+1) # 1~n의 팀
    graph = [[False] * (n+1) for _ in range(n+1)]
    last_year = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            graph[last_year[i]][last_year[j]] = True # 연결된거니까
            indegree[last_year[j]] += 1
    # 올해랑 바뀐 팀들
    for _ in range(int(input())):
        a, b = map(int, input().split())
        # 간선 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1
    # 위상정렬 시작
    result = []
    q = deque()
    # 0인애를 q에넣자
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    # 시작
    cycle = False # 사이클이 있는지 체크
    check = True # 위상정렬 결과가 1개인지 체크

    for i in range(n):
        # 사이클이 생겼을 경우
        if len(q) == 0:
            cycle = True
            break
        # 정답이 2개 이상인 경우
        if len(q) > 1:
            check = False
            break
        
        now = q.popleft()
        result.append(now)
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
    # 사이클 검사 -> IMPOSSIBLE
    if cycle:
        print("IMPOSSIBLE")
    # 사이클은 없지만, 답이 2개이상이라면
    elif not check:
        print("?")
    # 답이 있다면
    else:
        for i in result:
            print(i,end=' ')
        print()


    
