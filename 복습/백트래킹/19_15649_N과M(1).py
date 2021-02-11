n, m = map(int, input().split())
row = [0] * m

# 반복해서 돌 곳
def solve(depth):
    if depth == m:
        print(' '.join(map(str,row)))
        return
    
    for i in range(n): # i+1이 들어가야함
        row[depth] = i+1
        if check(depth):
            solve(depth+1)

# 조건 달아주는곳
def check(depth): 
    for i in range(depth): # depth이전까지 같은값이 없어야함
        if row[depth] == row[i]:
            return False
    return True

solve(0)
