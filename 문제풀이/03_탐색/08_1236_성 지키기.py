# 1/19
# 문제 난이도: Bronze 1
# 문제 유형: 탐색
# 추천 풀이 시간: 20분

# 모든 행과 모든 열에 한 명 이상의 경비원이 있어야 한다.
# 행기준으로 보았을 때 필요한 경비원 수 
# 열기준으로 보았을 때 필요한 경비원 수 
# 더 큰수를 출력한다

#################### ####################
n, m = map(int, input().split(' '))
array = []

for i in range(n):
    array.append(input())

l_x = [0] * n
l_y = [0] * m

for i in range(n):
    for j in range(m):
        if array[i][j] == 'X':
            l_x[i] = 1
            l_y[j] = 1

x_count = 0
for i in l_x:
    if i == 0:
        x_count += 1

y_count = 0
for i in l_y:
    if i == 0:
        y_count += 1
print(max(x_count,y_count))

#################### ####################
# 동빈나

n, m = map(int, input().split(' '))
array = []

for _ in range(n):
    array.append(input())

row = [0] * n
column = [0] * m

for i in range(n):
    for j in range(m):
        if array[i][j] == 'X':
            row[i] = 1
            column[j] = 1

row_count = 0
for i in row:
    if i == 0:
        row_count += 1

column_count = 0
for i in column:
    if i == 0:
        column_count += 1
print(max(row_count,column_count))
    