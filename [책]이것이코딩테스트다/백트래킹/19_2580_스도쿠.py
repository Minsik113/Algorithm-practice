# 9x9 스도쿠
row = [0] * 9 # 행기준) 0의 개수 파악
col = [0] * 9 # 열기준) 0의 개수 파악

array = []
num = 0

for i in range(9):
    data = list(map(int, input().split()))
    for i in range(9):
        if data[i] == 0:
            col[i] += 1 # 열마다 0 개수 저장
            row[num] += 1 # 행마다 0 개수 저장
    num += 1
    array.append(data)
print('row',row)
print('col',col)

# row체크
def row_solve():
    for i in range(9): # index = 0 ~ 8
        if row[i] == 1:
            r_check(i) # i번째 0인거 채워넣기.
# col체크
def col_solve():
    for i in range(9):
        if col[i] == 1:
            c_check(i)

# 0인거 채워넣는 함수
def r_check(i): # row[i]==1 or col[i]==1  i번째 행or열을 바꾸고싶다.
    visited = [False] * 10
    visited[0] = True
    pos = 0 # 0인곳의 열의 위치
    value = 0 # 필요한 숫자

    # 0인곳 위치 = pos . 이게 col도 됨.
    for j in range(9): # 없는 수를 찾자
        if array[i][j] == 0: 
            pos = j
        else:
            visited[j+1] = True

    # 필요한 숫자 = value
    for j in range(1,10):
        if not visited[j]: # False
            value = j
            break
    
    # array에 채워넣고, row[i] 값 수정하자
    array[i][pos] = value
    row[i] -= 1
    col[pos] -= 1

def c_check(i):
    visited = [False] * 10
    visited[0] = True
    pos = 0 # 0인곳의 열의 위치
    value = 0 # 필요한 숫자

    # 0인곳 위치 = pos . 이게 row도 됨.
    for j in range(9): # 없는 수를 찾자
        if array[j][i] == 0: 
            pos = j
        else:
            visited[j+1] = True

    # 필요한 숫자 = value
    for j in range(1,10):
        if not visited[j]: # False
            value = j
            break
    
    # array에 채워넣고, row[i] 값 수정하자
    array[pos][i] = value
    row[pos] -= 1
    col[i] -= 1
def box_solve(): # 0~2 3~5 6~8 번 보면됨

# row나 col중 0의개수 1인곳 확인해서 채워넣자.
while True:
    if sum(row) == 0 and sum(col) == 0:
        break
    row_solve()
    col_solve()
    box_solve()