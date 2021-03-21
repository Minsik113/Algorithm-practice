'''
(0,0) -> (n-1,n-1)까지의 최소거리는?
n = 125까지라서 다익스트라.

array[i][j] = i,j 까지 갈때까지 드는 최소비용?
보는순서는 상하좌우로 움직이므로 bfs로 봐야겠다.

'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(int(input())):
    n = int(input())
    
    # 1번. 맵정보를 입력받는다.
    graph = [list(map(int, input().split())) for _ in range(n)]

    # 2번. distance로 각점까지 걸리는 거리
    distance = [[INF] * n for _ in range(n)]
    # 3. 0,0 -> n-1, n-1 시작
    x, y = 0, 0
    distance[x][y] = graph[x][y]
    q = []
    heapq.heappush(q, (graph[x][y], x, y))
    while q:
        # 가장 최단 거리가 짧은 노드에 대해 꺼낸다
        dist, x, y = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있다면 무시
        if distance[x][y] < dist:
            continue
        # 현재노드와 연결된 다른 인접한 노드들을 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            cost = dist + graph[x][y]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧을 경우
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    print(distance)

