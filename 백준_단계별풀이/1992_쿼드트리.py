##########################################
##########################################
# 3/26 - 다른원소가 보이면 바로 4등분함
import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().rstrip())) for _ in range(n)]
result = ''

def cut(a, b, array, length):
    global result

    pre = array[a][b]
    for i in range(a, a+length):
        for j in range(b, b+length):
            if pre != array[i][j]:
                # 4등분한다
                result += '('
                for x in range(2):
                    for y in range(2):
                        cut(a+length//2*x, b+length//2*y, array, length//2)
                # 등분했으면 리턴함
                result += ')'
                return

    if pre == 1:
        result += '1'
    elif pre == 0:
        result += '0'

cut(0, 0, data, n)
print(result)

##########################################
##########################################
# 3/26 - 쭉 다보고 판단하는거. 느림.
'''
'분할'하면서 해결하는 문제이다.
재귀를 써야하는문제
def calculator(a,b,array,length) 
-> (시작좌표, 배열, 배열길이)를 넘긴다
왼위     a, b
오른위   a, b+n//2
왼아래   a+n//2, b
오른아래 a+n//2, b+n//2
'''
# n = int(input())
# data = [list(map(int, input())) for _ in range(n)]
# result = ''

# def calculator(a, b, array, length):
#     global result
#     # 1. array의 원소들을 본다
#     total = 0 
#     for i in range(a, a+length):
#         for j in range(b, b+length):
#             if array[i][j] == 1:
#                 total += 1
#     # 2. 모두 0인경우
#     if total == 0: 
#         result += '0'
#     # 3. 모두 1인경우
#     elif total == length*length:
#         result += '1'
#     # 4. 값이 다른경우 4등분한다
#     else:
#         result += '('
#         k = length // 2
#         calculator(a, b, array, k) # 왼위
#         calculator(a, b+k, array, k) # 오른위
#         calculator(a+k, b, array, k) # 왼아래
#         calculator(a+k, b+k, array, k) # 오른아래
#         result += ')'

# calculator(0, 0, data, n)
# print(result)