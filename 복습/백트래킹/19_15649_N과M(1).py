##########################################
##########################################
# 3/20 복습
n, m = map(int, input().split())
data = [i for i in range(1,n+1)]
row = [0] * m

# 이전에 x가 들어왔었는지 체크한다
def check(x, index): # index위치에 x가들어간거니 index전까지본다
    for j in range(index):
        if row[j] == x:
            return False
    return True

def solve(depth):
    # 원하는만큼 뽑았으면 출력해야함
    if depth == m:
        print(" ".join(map(str, row)))
        return
    # 원하는만큼 못 뽑았다면 수 넣어봐야함
    for i in range(len(data)):
        if check(data[i], depth): # depth위치에 data[i]를 넣어도 되는가?
            # 넣어도된다 -> 넣고, 다음depth로이동
            row[depth] = data[i] 
            solve(depth + 1) 
            row[depth] = 0 # 끝난다면 0으로 다시바꿔줌
solve(0)
##########################################
##########################################
#
# n, m = map(int, input().split())
# row = [0] * m

# # 반복해서 돌 곳
# def solve(depth):
#     if depth == m:
#         print(' '.join(map(str,row)))
#         return
    
#     for i in range(n): # i+1이 들어가야함
#         row[depth] = i+1
#         if check(depth):
#             solve(depth+1)

# # 조건 달아주는곳
# def check(depth): 
#     for i in range(depth): # depth이전까지 같은값이 없어야함
#         if row[depth] == row[i]:
#             return False
#     return True

# solve(0)
