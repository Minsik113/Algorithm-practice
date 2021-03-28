# '''
# 1. 우선순위큐로 2개뽑아서 합해서 다시넣는다.
# 2. 합한값을 따로 result에 저장함
# 3. 1,2반복한다. 리스트길이가 1이되면 반복문나온다
# 4. result 출력

# nC2  n-1C2 ... 2C2 를 n번더해야함
# O(N^3) = 500**3 => 안됨

# 중복되는 계산이 있는지 본다.
# ABCDE
# f(p, q) = (f(p, p) + f(p+1, q) or f(p, p+1)+f(p+2, q) or ...)
# A BCDE or AB CDE or ...
#     A   B   C                   D                   E
# A   0   AB  MIN(AB,BC) + ABC    
#             (BC + ABC)          AB + CD + ABCD
# B       0   BC                  MIN(BC,CD) +BCD
#                                 (BC + BCD)
# C           0                   CD
# D                               0
# E                                                   0

# [I][J] I부터J까지가는데 드는 작은비용을 넣자
# F(A, D) = min(f(A, A) + f(B, d) ,   # BC + BCD => 60 + 110 
#                 f(A, B) + f(C, D),  # AB + CD  => 70 + 80 
#                 f(A, C) + f(D, D))  # BC + ABC => 60 + 130
# 걸리는시간은 o(n^2) O에 N square가 된다.
# '''
# import sys, math
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n = int(input())
#     arr = [int(x) for x in input().split()]
#     rst = [[0 for _ in range(n)] for _ in range(n)]
#     for j in range(1, n):
#         for i in range(j-1, -1, -1):
#             small = math.inf
#             for k in range(j-i):
#                 small = min(small, rst[i][i+k] + rst[i+k+1][j])
#             rst[i][j] = small + sum(arr[i:j+1])
#     print(rst[0][n-1]) 
#     # [i][j] = index가 i부터 j까지의 수까지 합칠 때 드는 최소비용