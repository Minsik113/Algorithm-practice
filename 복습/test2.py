n, m = map(int, input().split())
data = [i for i in range(1, n+1)]
row = [0] * m

def check(x, depth): # x를 depth위치에 넣어도되는가
    # 이전값들이 작거나 같아야한다.
    for j in range(depth):
        if row[j] > x:
            return False
    return True

def solve(depth):
    # 개수다찼으니 결과물 내보낸다.
    if depth == m:
        print(" ".join(map(str, row)))
        return
    # 개수 다 안됐으니까 만들어준다.
    for i in range(len(data)):
        # data[i]를 depth위치에 넣어도 되는가? 
        if check(data[i], depth):
            row[depth] = data[i] # 넣어도되니까 넣는다
            solve(depth + 1) # 다음꺼 본다.
            row[depth] = 0 # 다시 원상복구해주고 다른애 넣는다.

solve(0)