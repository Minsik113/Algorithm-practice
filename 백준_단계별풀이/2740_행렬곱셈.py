# 풀이 1
'''
n,m
A = nxm
m,k
B = mxk

n x k 가 만들어짐
A의 i행의 모든 원소들과 B의 i열의 모든 원소들의 곱을 합해라
'''
n, _ = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(m)]

for i in range(n):
    for j in range(k):
        save = 0
        for x in range(m):
            save += A[i][x] * B[x][j]
        print(save, end=' ')
    print()

# 풀이2
# n, _ = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(n)]
# m, k = map(int, input().split())
# B = [list(map(int, input().split())) for _ in range(m)]

# data = [[0] * k for _ in range(n)]
# for i in range(n):
#     for j in range(k):
#         save = 0
#         for x in range(m):
#             save += A[i][x] * B[x][j]
#         data[i][j] = save
# for i in range(n):
#     for j in range(k):
#         print(data[i][j], end=' ')
#     print()