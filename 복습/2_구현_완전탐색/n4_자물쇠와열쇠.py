'''
완전탐색

20 x 20 -> 400연산.
-> n을 3배크게해서 왼쪽모서리부터 보자.
'''
# 시계방향 90도 회전
def rotate_90(a):
    n = len(a) # 행길이
    m = len(a[0]) # 열길이
    array = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            array[j][n-i-1] = a[i][j]
    return array

# 자물쇠의 중간부분이 모두 1인지 체크하자
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠 크기 3배로 확장
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    # new_lock의 중앙부분에 기존 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
            
    # 4방향에 대해서 확인
    for _ in range(4): 
        key = rotate_90(key)
        for x in range(n*2): # 자물쇠가 n크기니까
            for y in range(n*2):
                # 자물쇠에 열쇠 꼽아보기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                # 자물쇠 체크
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
solution(key, lock)