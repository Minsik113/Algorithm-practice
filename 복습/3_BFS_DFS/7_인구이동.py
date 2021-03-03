'''
1. 연결관계 찾기
1-1. 연결관계에서의 총 합
1-2. 연결관계에서의 총 개수
2. 봤던 도시인지 체크함
3. 안봤던 도시중 다음 연결관계로 넘어감
4. 한바퀴돌면 result += 1
5. 1234반복
'''
from collections import deque

n, l, r = map(int, input().split())
# 도시정보 입력받는다.
graph = [list(map(int,input().split())) for _ in range(n)]

# (i,j)에서 l~r에 속하는지 탐색
dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1]
def solve(visited, graph, i, j): # 연결리스트 1개라도 나오면 True임
    visited[i][j] = 1
    q = deque()
    q.append((i,j))
    total = graph[i][j] # 연결그래프의 총 인구 수
    count = 1 # 연결그래프의 총 도시 수
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 봤던 도시인지 체크 -> abs()조건 확인
            if visited[nx][ny] == 0:
                if abs(graph[x][y] - graph[nx][ny]) >= l and abs(graph[x][y] - graph[nx][ny]) <= r:
                    print('들어옴?')
                    count += 1
                    total += graph[nx][ny]
                    visited[nx][ny] = 1
    print(graph)
    print(visited)
    print('답',count)
    # 바뀐게 없다면 count == 1 임
    if count == 1:
        return False
    temp = int(total/count)
    for x in range(n):
        for y in range(n):
            if visited[x][y] == 1:
                graph[x][y] == temp
    return True

# 탐색 시작
result = 0
num = 0
while True:
    change = False
    # 방문도시 체크
    visited = [[0]*(n) for _ in range(n)] # 매번 초기화 시킴
    # 연결관계 찾아야한다
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0: # 안본도시라면 
                if solve(visited, graph, i, j): # 연결리스트 1개라도 나오면 True임
                    print("???")
                    change = True # 바뀐게 하나라도 있음.
    if num == 4:
        exit()
    num+= 1
    # 변한게 없다면 종료
    if not change: 
        print(result)
        break
