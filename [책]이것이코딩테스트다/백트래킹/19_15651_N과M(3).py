##########################################
##########################################
# 3/20 복습
n, m = map(int, input().split())
data = [i for i in range(1, n+1)]
row = [0] * m # m개 만들꺼니까

def solve(depth):
    # 개수다 차면 출력
    if depth == m:
        print(" ".join(map(str, row)))
        return
    # 데이터를 넣어준다
    for i in range(len(data)):
        row[depth] = data[i]
        solve(depth + 1)
        row[depth] = 0

solve(0)

##########################################
##########################################
# 
# n, m = map(int, input().split())
# row = [0] * m

# def solve(depth):
#     if depth == m:
#         print(' '.join(map(str, row)))
#         return
#     for i in range(n):
#         row[depth] = i+1
#         # if check(depth): # depth행에 들어간 i 를 체크하기위해서
#         solve(depth+1)

# solve(0)
