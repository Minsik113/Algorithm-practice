'''
1. 맵입력받음
2. 장애물3개설치
-> Combination써도 36C3이라 3만안됨
3. 각 선생님에 대해서 학생보이는지 체크
4. 한명이라도 학생이 보인다면 break하고 장애물 다시설치
5. 모든 선생님에 대해 학생이 안보이면 "YES" + 종료
'''
##########################################
##########################################
# (x,y) in 으로 위치찾기식으로도 해보자

##########################################
##########################################
# graph[i][j] 를 바꾸는식으로
from itertools import combinations

n = int(input())
# 맵 입력받음
graph = [list(map(str,input().split())) for _ in range(n)]
# 각각의 위치 찾음
possible = []
teacher = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
            possible.append((i,j))
        elif graph[i][j] == 'T':
            teacher.append((i,j))
# 선생위치에서 상하좌우로 쭉 감
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def check(graph,teacher):
    for j in range(len(teacher)):
        x, y = teacher[j]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 범위 밖 or 장애물 = 다음 방향 보자
            if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 'O': 
                continue
            # 학생이 있는지 체크
            go = True
            while True:
                # 범위 밖 or 장애물 = 그만 봐도 된다
                if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 'O': 
                    break
                if graph[nx][ny] == 'S': 
                    go = False
                    break
                nx += dx[k]
                ny += dy[k]
            if not go: # 직선방향 보다가 학생 만남
                return False
    return True # 학생 안마주쳤다는거니까 True

# 장애물 들어갈 수 있는 위치 등록
result = False
count = 0
for i in combinations(possible, 3):
    v1, v2, v3 = i
    flag = True
    # 장애물 넣는다
    graph[v1[0]][v1[1]] = 'O'
    graph[v2[0]][v2[1]] = 'O'
    graph[v3[0]][v3[1]] = 'O'
    # 선생님 위치에서 학생 찾기 START
    if not check(graph,teacher): # 학생만났으니 원상복구
        graph[v1[0]][v1[1]] = 'X'
        graph[v2[0]][v2[1]] = 'X'
        graph[v3[0]][v3[1]] = 'X'
        flag = False
    # 모든선생한테서 학생 안만나서 True니까 성공함. 종료.
    if flag: 
        result = True
        break

if result:
    print("YES")
else:
    print("NO")
