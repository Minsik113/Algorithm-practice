'''
총 8방향 체크해야한다.
해당위치에서 범위벗어나는지 체크한다
-> 8 - 벗어나는횟수
'''
##########################################
##########################################
# 
strings = input()
row = int(strings[1])
col = int(ord(strings[0])) - int(ord('a')) + 1


##########################################
##########################################
# 내 방법-
dx = [-2,-2,-1,1,2,2,1,-1] # 북 동 남 서
dy = [-1,1,2,2,1,-1,-2,-2] 
strings = input()
tree = dict()
tree['a'] = 1
tree['b'] = 2
tree['c'] = 3
tree['d'] = 4
tree['e'] = 5
tree['f'] = 6
tree['g'] = 7
tree['h'] = 8
count = 8
x, y = int(strings[1]), tree[strings[0]]
for i in range(8):
    nx = dx[i] + x
    ny = dy[i] + y
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        count -= 1
print(count)