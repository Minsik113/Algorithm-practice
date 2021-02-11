n, m = map(int, input().split())
row = [0] * m

def solve(depth):
    if depth == m:
        print(' '.join(map(str, row)))
        return 
    for i in range(n):
        row[depth] = i+1
        if check(depth):
            solve(depth+1)
# 조건 달아
def check(depth):
    for i in range(depth):
        if row[depth] <= row[i]: # 이전 값들보다 커야함.
            return False
    return True

solve(0)
