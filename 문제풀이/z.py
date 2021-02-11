N, R, C = map(int, input().split())
# 2^N x 2^N의 정사각형.
# 정사각형의 R행 C열의 수를 찾아라
count = 0
# row = [[] for i in range(2**N)]
def solve(n, x, y):
    if n == 0: # 왼쪽맨위부터 계산시작.
        # 배열[]?? = count
        count += 1
        pass
    
    solve(n//2, x, y)
    solve(n//2, x, y + n//2)
    solve(n//2, x + n//2, y)
    solve(n//2, x + n//2, y + n//2)


solve(N, 0, 0)
