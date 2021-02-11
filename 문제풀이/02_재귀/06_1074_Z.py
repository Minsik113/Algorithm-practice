# 1/18 
# 문제 난이도 : Silver 1
# 문제 유형: 재귀
# 추천 풀이 시간: 40분

# 2^N x 2^N 모양의 정사각형
# 입력: N r c
# 출력: r행 c열을 몇 번째로 방문했는지 출력한다.

# 2^N x 2^N 모양의 정사각형
# 입력: N r c
# 출력: r행 c열을 몇 번째로 방문했는지 출력한다.


# 1. Z 모양을 구성하는 4가지 방향에 대하여 차례대로 재귀적으로 호출한다.
# 1  4     0,0   0,2
# 
# 8  12    2,0   2,2 
# 

# 나동빈

def solve(n, x, y):
    global result 
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1

        if x == X and y+1 == Y:
            print(result)
            return
        result += 1

        if x+1 == X and y == Y:
            print(result)
            return
        result += 1

        if x+1 == X and y+1 == Y:
            print(result)
            return
        result += 1
        return
    solve(n/2, x, y) # 왼위
    solve(n/2, x, y+n/2) # 오른위
    solve(n/2, x+n/2, y) # 왼아래
    solve(n/2, x+n/2, y+n/2) #오른아래

result = 0
N, X, Y = map(int, input().split(' '))
solve(2**N, 0, 0) # 시작점 0,0


