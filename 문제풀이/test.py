from collections import deque

test = int(input())

for _ in range(test):
    n = int(input())
    # 작년 순위정보
    last_year = list(map(int, input().split()))
    # 진입차수
    indegree = [0] * (n+1)
    # 간선정보 담기위한 인접행렬 
    # 작년 순위
    graph = [ [False]*(n+1) for _ in range(n+1)] 
    for i in range(n):
        for j in range(i+1, n):
            graph[last_year[i]][last_year[j]] = True # i -> j
            indegree[last_year[j]] += 1 # j += 1

    # 올해 순위
    m = int(input())
    for i in range(m):
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
    # 위상정렬 
    result = []
    q = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    
    check = True # 위상정렬 결과가 1개인지 체크
    cycle = False # 사이클 있는지 체크

    for i in range(n):
        # 모든 노드 보기전에 cycle이 생기는지 체크
        if len(q) == 0:
            cycle = True
            break
        # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개
        if len(q) >= 2:
            check = False
            break
        
        now = q.popleft()
        result.append(now)
        # now와 연결된 노드들의 진입차수 빼자
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
    # 사이클 -> "IMPOSSIBLE"
    if cycle:
        print("IMPOSSIBLE")
    # 결과 여러개라면 -> "?"
    elif not check:
        print("?")
    else:
        for i in result:
            print(i,end=' ')
        print()
