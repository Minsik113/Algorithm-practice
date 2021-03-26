##########################################
##########################################
# 3/26 - 같지않은 수 나오면 바로 9등분 하기
import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
result = [0] * 3 

def cut(a, b, array, length):
    pre = array[a][b]
    for i in range(a, a+length):
        for j in range(b, b+length):
            if pre != array[i][j]:
                # 9등분해라
                for x in range(3):
                    for y in range(3):
                        cut(a+length//3*x, b+length//3*y, array, length//3)
                return
    # 모든원소가 같으면 이쪽으로 온다
    if pre == -1:
        result[0] += 1
    elif pre == 0:
        result[1] += 1
    elif pre == 1:
        result[2] += 1

cut(0, 0, data, n)
for i in result:
    print(i)

##########################################
##########################################
# 3/26 - 시간초과 코드
'''
분할정복 - 분할해서 확인해라. (재귀)
n = 3^7 = 2200
n^n = 약4500000
2초면 배열계속보면서해도 충분할것같은데;;

1. 들어온배열의 합을 본다. (음수, 0, 양수 )
2. 모두같다면 어떤원소로 같은지를 리스트에서 체크해준다
'''
# import sys
# input = sys.stdin.readline

# n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)]
# result = [0] * 3 # -1, 0, 1 의 개수를 저장할 리스트

# def calculator(a, b, array, length):
#     global result
#     # 1.
#     count_l = 0 # -1
#     count = 0 # 0
#     count_r = 0 # 1
#     for i in range(a, a+length):
#         for j in range(b, b+length):
#             if array[i][j] == -1:
#                 count_l += 1
#             elif array[i][j] == 1:
#                 count_r += 1
#             else:
#                 count += 1
#     # 2. array가 같은 수 라면
#     if count_r == length*length or count == length*length or count_l == length*length:
#         # 시작점 -1=0  0=1  1=2
#         result[array[a][b]+1] += 1 
#     # 3. 섞여있다면 9등분해서 봐라
#     else:
#         k = length // 3
#         calculator(a, b, array, k) # 왼위
#         calculator(a+k, b, array, k) # 왼중간
#         calculator(a+2*k, b, array, k) # 왼아래
#         calculator(a, b+k, array, k) # 중간위
#         calculator(a+k, b+k, array, k) # 중간중간
#         calculator(a+2*k, b+k, array, k) # 중간아래
#         calculator(a, b+2*k, array, k) # 오른위
#         calculator(a+k, b+2*k, array, k) # 오른중간
#         calculator(a+2*k, b+2*k, array, k) # 오른아래
#     return

# calculator(0, 0, data, n)
# for i in result:
#     print(i)