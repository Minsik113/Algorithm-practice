''' 백트래킹은 완전탐색, BFS, DFS와 유사하다.
# 1/31
# 문제 난이도: Gold 4
# 문제 유형: 백트래킹
# 추천 풀이 시간: 40분

지금까지 지나온 모든 칸에 적혀 있는 알파벳과 다른 알파벳이 적힌 칸으로 이동
r과 c가 20이하이므로 백트래킹을 이용하여 모든 경우의 수를 고려하자.

이동하는 경로를 문자열 형태로 처리하면 간단하게 풀 수 있다.
'''


############ ###########
# 동빈나 

# 상 하 좌 우
dx = [-1,1,0,0] 
dy = [0,0,-1,1]

def bfs(x, y):
    global result
    # 동일한 경우는 한 번만 계산하기 위해서 집합(Set) 자료형 사용
    q = set()
    q.add((x,y,array[x][y]))
    while q:
        x, y, step = q.pop()
        # 가장 긴 이동거리를 저장
        result = max(result, len(step))

        # 네 방향으로 이동하는 경우를 각각 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 이동할 수 있는 위치이면서, 새로운 알파벳인 경우
            if (0 <= nx and nx < r and 0 <= ny and ny < c and
                array[nx][ny] not in step):
                q.add((nx, ny, step + array[nx][ny]))

r, c = map(int, input().split())
array = []
for _ in range(r):
    array.append(input())

result = 0
bfs(0, 0)
print(result)