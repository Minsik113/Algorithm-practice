n, m = map(int, input().split())
row = [0] * m

def solve(depth):
    if depth == m:
        print(' '.join(map(str, row)))
        return
    for i in range(n):
        row[depth] = i+1
        # if check(depth): # depth행에 들어간 i 를 체크하기위해서
        solve(depth+1)

solve(0)
