##########################################
##########################################
# 3/20 복습
n, m = map(int, input().split())
data = [i for i in range(1, n+1)]
row = [0] * m

def check(x, index):
    for j in range(index):
        if row[j] >= x: # 이전애들이 x보다 크면 False
            return False
    return True


def solve(depth):
    # 다찼으면 계싼
    if depth == m:
        print(" ".join(map(str, row)))
        return
    # 다안찼으면 넣는다
    for i in range(len(data)):
        if check(data[i], depth): # data[i]를 depth위치에 넣어도될까?
            row[depth] = data[i] # 넣고
            solve(depth+1) # 다음꺼보고
            row[depth] = 0# 원상복구

solve(0)
##########################################
##########################################
# #
# n, m = map(int, input().split())
# row = [0] * m

# def solve(depth):
#     if depth == m:
#         print(' '.join(map(str, row)))
#         return 
#     for i in range(n):
#         row[depth] = i+1
#         if check(depth):
#             solve(depth+1)
# # 조건 달아
# def check(depth):
#     for i in range(depth):
#         if row[depth] <= row[i]: # 이전 값들보다 커야함.
#             return False
#     return True

# solve(0)
