'''
총 8방향 체크해야한다.
해당위치에서 범위벗어나는지 체크한다
-> 8 - 벗어나는횟수
'''
##########################################
##########################################
# 
data = input()
row = int(data[1]) - 1 # 0~7까지로 나타낼것이다.
col = ord(data[0]) - ord('a') # a라면 0임.

array = [[0]*8 for _ in range(8)]
dx = [-2,-2,-1,1,2,2,1,-1] # 북 동 남 서
dy = [-1,1,2,2,1,-1,-2,-2]

result = 0

for i in range(8):
    nx = row + dx[i]
    ny = col + dy[i]

    if nx < 0 or ny < 0 or nx >= 8 or ny >= 8:
        continue
    result += 1
print(result)

##########################################
##########################################
# 내 방법-
# dx = [-2,-2,-1,1,2,2,1,-1] # 북 동 남 서
# dy = [-1,1,2,2,1,-1,-2,-2] 
# strings = input()
# tree = dict()
# tree['a'] = 1
# tree['b'] = 2
# tree['c'] = 3
# tree['d'] = 4
# tree['e'] = 5
# tree['f'] = 6
# tree['g'] = 7
# tree['h'] = 8
# count = 8
# x, y = int(strings[1]), tree[strings[0]]
# for i in range(8):
#     nx = dx[i] + x
#     ny = dy[i] + y
#     if nx < 1 or ny < 1 or nx > 8 or ny > 8:
#         count -= 1
# print(count)