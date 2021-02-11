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

def check(depth):
    for i in range(depth):
        if row[i] > row[depth]:
            return False
    return True

solve(0)