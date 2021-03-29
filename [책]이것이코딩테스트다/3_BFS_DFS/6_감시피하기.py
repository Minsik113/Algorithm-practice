
##########################################
##########################################
# (x,y) in 으로 위치찾기식으로도 해보자
'''
3개의 장애물설치
모든학생들이 선생님들시야에 안보이게 해라
선생님들은 해장좌표에서 상하좌우 직선으로만 가능.

놓을 수 있는 3곳의 좌표를 저장함.
각좌표에 대해 설치해보면서 파악.

모든 학생위치에서 선생 안만나면됨.

1. 맵입력받음
2. '장애물을 놓을 수 있는 위치', '선생위치'저장
2-1. 3개씩묶인 장애물 리스트를 만든다
3. 장애물리스트중 하나를 꺼내 장애물 설치
4. 학생위치에서 상하좌우로 쭉 본다. 선생안만나면 다음 학생위치본다.
5. 모든 학생들이 선생안만났다면 "yes"
5-1. 선생만났다면 장애물 다시설치한다.
'''
from itertools import permutations
from collections import deque

n = int(input())
# 1.
array = [list(map(str, input().split())) for _ in range(n)]
# 2.
students = [] # 학생들위치
xposition = [] # 설치할 수 있는 곳
for i in range(n):
    for j in range(n):
        if array[i][j] == 'S':
            students.append((i,j))
        elif array[i][j] == 'X':
            xposition.append((i,j))
# 2-1.
possible = [] # 설치가능한 장애물 3곳의 조합리스트
for i in permutations(xposition, 3):
    possible.append(list(i))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
flag = False # True가 되면 'yes'
while possible:
    v1, v2, v3 = possible.pop()
    # 3. 맵에 v1,v2,v3을 장애물로 표시한다
    array[v1[0]][v1[1]] = 'O'
    array[v2[0]][v2[1]] = 'O'
    array[v3[0]][v3[1]] = 'O'
    # 3-1. 학생들위치에서 방위를 확인하자. -> 하나라도 'T'만나면 장애물 다시설치.
    restart = False
    for student in students:
        x, y = student
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or array[nx][ny] == 'O':
                continue
            # 가능한애들중에서 i방향을 쭉보며 선생님이 있는지
            # 3-2. 선생님 만나면 -> 장애물 다시설치한다.
            if array[nx][ny] == 'T': 
                restart = True
                break
            # 3-3. 'X', 'S'라면 해당방향으로 쭉 본다
            elif array[nx][ny] == 'X' or array[nx][ny] == 'S':
                while True:
                    nx += dx[i]
                    ny += dy[i]
                    # 범위넘거나 'O'만나면 나온다.
                    if nx < 0 or ny < 0 or nx >= n or ny >= n or array[nx][ny] == 'O':
                        break 
                    # 3-3-1. 'T'만나면 더 안봐도된다. 
                    if array[nx][ny] == 'T':
                        restart = True
                        break
                    # 3-3-2. 'X'or'S'는 그다음방향도 봐야함
        # 장애물 다시설치 -> 학생 볼 필요없다.
        if restart:
            break    
    # 모든학생 -> 성공적으로 안만났다면 "yes"하고 종료.
    if not restart:
        flag = True
        break
    # 장애물로 바꿧던곳을 다시 x로 바꾼다
    array[v1[0]][v1[1]] = 'X'
    array[v2[0]][v2[1]] = 'X'
    array[v3[0]][v3[1]] = 'X'

if flag:
    print("YES")
else:
    print("NO")
##########################################
##########################################
'''
1. 맵입력받음
2. 장애물3개설치
-> Combination써도 36C3이라 3만안됨
3. 각 선생님에 대해서 학생보이는지 체크
4. 한명이라도 학생이 보인다면 break하고 장애물 다시설치
5. 모든 선생님에 대해 학생이 안보이면 "YES" + 종료
'''
# graph[i][j] 를 바꾸는식으로
# from itertools import combinations

# n = int(input())
# # 맵 입력받음
# graph = [list(map(str,input().split())) for _ in range(n)]
# # 각각의 위치 찾음
# possible = []
# teacher = []
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 'X':
#             possible.append((i,j))
#         elif graph[i][j] == 'T':
#             teacher.append((i,j))
# # 선생위치에서 상하좌우로 쭉 감
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# def check(graph,teacher):
#     for j in range(len(teacher)):
#         x, y = teacher[j]
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             # 범위 밖 or 장애물 = 다음 방향 보자
#             if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 'O': 
#                 continue
#             # 학생이 있는지 체크
#             go = True
#             while True:
#                 # 범위 밖 or 장애물 = 그만 봐도 된다
#                 if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 'O': 
#                     break
#                 if graph[nx][ny] == 'S': 
#                     go = False
#                     break
#                 nx += dx[k]
#                 ny += dy[k]
#             if not go: # 직선방향 보다가 학생 만남
#                 return False
#     return True # 학생 안마주쳤다는거니까 True

# # 장애물 들어갈 수 있는 위치 등록
# result = False
# count = 0
# for i in combinations(possible, 3):
#     v1, v2, v3 = i
#     flag = True
#     # 장애물 넣는다
#     for x,y in i:
#         graph[x][y] = 'O'
#     # graph[v1[0]][v1[1]] = 'O' 위처럼 바꿀 수 있다.
#     # graph[v2[0]][v2[1]] = 'O'
#     # graph[v3[0]][v3[1]] = 'O'
#     # 선생님 위치에서 학생 찾기 START
#     if not check(graph,teacher): # 학생만났으니 원상복구
#         for x, y in i:
#             graph[x][y] = 'X'
#         # graph[v1[0]][v1[1]] = 'X' #위처럼 바꾸기가능
#         # graph[v2[0]][v2[1]] = 'X'
#         # graph[v3[0]][v3[1]] = 'X'
#         flag = False
#     # 모든선생한테서 학생 안만나서 True니까 성공함. 종료.
#     if flag: 
#         result = True
#         break

# if result:
#     print("YES")
# else:
#     print("NO")
