'''
다익스트라로 0,0 -> n-1, n-1구하면됨

'''
import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(int(input())):
    n = int(input())
    # 1번. 맵 입력받자
    data = [list(map(int, input().split())) for _ in range(n)]
    
    # 2번. distance 선언 및 초기화
    distance = [[INF] * n for _ in range(n)]
    x, y = 0, 0
    distance[x][y] = data[x][y] 
    h = []
    heapq.heappush(h, (distance[x][y], x, y))

    while h:
        dist, x, y = heapq.heappop(h)
        # 이미 더 작은것으로 되어있다면 볼 필요가 없다. -> 더작은값으로 이미 갱신을 맞췄으니까
        if distance[x][y] < dist:
            continue
        # 4방위에 대해서 보자
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            cost = dist + data[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(h, (cost, nx, ny))
    
    print(distance[n-1][n-1])                
