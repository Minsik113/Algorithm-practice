'''
lock은 가만히 있을것임.
key를 돌리면서 비교할것임.
key가 lock보다 크면서 lock이 안닿는 부분에 key의돌기가 있다면 애초에 FALSE임.

lock을 3배크기로 늘리고 정가운데에 lock배치 (0,0)부터 key배치해서옆으로이동.끝까찌갈떄까지.
키돌려서도 넣어봄.
 if 가운데부분이 전부 1이라면 True . 종료
 else: 다음칸넘어감
 
1 2 3   7 4 1
4 5 6   8 5 2
7 8 9   9 6 3
2,0 ->0,0
1,0 ->0,1
2,1 ->1,0
'''
# 시계방향으로 90도 회전하는 함수
def turn90(data):
    length = len(data)
    array = [[0] * length for _ in range(length)]
    
    for i in range(length):
        for j in range(length):
            array[i][j] = data[length-j-1][i]
            
    return array
# 3배로 키워주는 함수
def three_multi(data):
    length = len(data) * 3
    l = len(data)
    array = [[0] * length for _ in range(length)]
    for i in range(len(data)):
        for j in range(len(data)):
            array[i+l][j+l] = data[i][j]
    return array

def solution(key, lock):
    three_lock = three_multi(lock)
    # 방향 4개로 돌려서 볼것이므로 4번 반복
    for _ in range(4):
        key = turn90(key)
    # 3배짜리 lock에 열쇠 넣어본다.
        for i in range(0, len(three_lock) - len(key)):
            for j in range(0, len(three_lock) - len(key)):

                # 열쇠를 넣어본다
                for x in range(len(key)):
                    for y in range(len(key)):
                        three_lock[i+x][j+y] += key[x][y]
                # 열쇠가 딱 맞는지 본다
                flag = True
                for x in range(len(lock), len(lock)*2):
                    for y in range(len(lock), len(lock)*2):
                        if three_lock[x][y] != 1:
                            flag = False
                            break
                    if flag == False:
                        break
                # 딱 맞으면 종료
                if flag:
                    return True
                # 다르면? 원상복구한다
                else:
                    for x in range(len(key)):
                        for y in range(len(key)):
                            three_lock[i+x][j+y] -= key[x][y]
    
    return False
# '''
# 1. Lock의 3배 크기를 만든다. 가운데를 lock으로 만듦.
# 2. key를 3Lock처음부터 넣어본다. 그때 lock부분이 다 1이라면 True.
# 3. 3Lock의 끝까지 다 넣어봤는데 못넣으면 False
# -> N=20일때 3N = 60  60x60을 m크기로봐야함
# (60-m)x(60-m)x4 = 열쇠도리면서 전부다 봄. 3600x4 = 시간안에 충분.
# ->
# 1. key를 4방향 돌리는함수
# 2. 3배Lock크기를 만든다.
# 3. key를 3Lock에 하나씩 넣어봄
# '''
# ##########################################
# ##########################################
# # 
# # 시계방향 90도 돌리는 함수
# def turn_right90(array):
#     length = len(array[0])
#     n_array = [[0]*length for _ in range(length)]
#     for i in range(length):
#         for j in range(length):
#             n_array[j][length-i-1] = array[i][j]
#     return n_array
# # 3배크기의 Lock을 만든다.
# def three_lock(array):
#     length = len(array)
#     n_array = [[0]*(3*length) for _ in range(3*length)]
#     # 가운데에 lock채움
#     for i in range(length):
#         for j in range(length):
#             n_array[i+length][j+length] = array[i][j]
#     return n_array
# # 자물쇠의 중간 부분이 모두 1인지 체크
# def check_lock(check_lock):
#     lock_length = len(check_lock) // 3
#     for i in range(lock_length, lock_length*2):
#         for j in range(lock_length, lock_length*2):
#             if check_lock[i][j] != 1:
#                 return False
#     return True
    
# def solution(key, lock):
#     answer = 0 
#     n = len(lock)
#     m = len(key)
#     # 3배lock만들기
#     new_lock = three_lock(lock)
    
#     # key랑 3lock비교 START
#     for i in range(4): # 4번 방향 바꿔서 봄
#         key = turn_right90(key)
#         for x in range(n*2):
#             for y in range(n*2):
#                 # 자물쇠에 열쇠 끼워넣기
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+j] += key[i][j]
#                 # 자물쇠에 열쇠가 정확히 들어맞는지 검사
#                 if check_lock(new_lock) == True:
#                     return True
#                 # 자물쇠에서 열쇠 빼자
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+j] -= key[i][j]
#     return False
# ##########################################
# ##########################################
# # 
# # 시계방향 90도 회전
# def rotate_90(a):
#     n = len(a) # 행길이
#     m = len(a[0]) # 열길이
#     array = [[0] * n for _ in range(m)]
#     for i in range(n):
#         for j in range(m):
#             array[j][n-i-1] = a[i][j]
#     return array

# # 자물쇠의 중간부분이 모두 1인지 체크하자
# def check(new_lock):
#     lock_length = len(new_lock) // 3
#     for i in range(lock_length, lock_length*2):
#         for j in range(lock_length, lock_length*2):
#             if new_lock[i][j] != 1:
#                 return False
#     return True

# def solution(key, lock):
#     n = len(lock)
#     m = len(key)
#     # 자물쇠 크기 3배로 확장
#     new_lock = [[0]*(n*3) for _ in range(n*3)]
#     # new_lock의 중앙부분에 기존 자물쇠 넣기
#     for i in range(n):
#         for j in range(n):
#             new_lock[i+n][j+n] = lock[i][j]
            
#     # 4방향에 대해서 확인
#     for _ in range(4): 
#         key = rotate_90(key)
#         for x in range(n*2): # 자물쇠가 n크기니까
#             for y in range(n*2):
#                 # 자물쇠에 열쇠 꼽아보기
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+j] += key[i][j]
#                 # 자물쇠 체크
#                 if check(new_lock) == True:
#                     return True
#                 # 자물쇠에서 열쇠빼기
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+j] -= key[i][j]
#     return False
# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# solution(key, lock)
