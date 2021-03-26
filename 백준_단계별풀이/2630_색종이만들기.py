##########################################
##########################################
# 3/26 - 재귀 - 범위 확실히
'''
왼위        a, b
오른위      a, b + n//2
왼아래      a + n//2, b
오른아래    a + n//2, b + n//2
'''
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
result = [0] * 2 # [0]=흰, [1]=파

def calculator(a, b, array, length):
    global result

    k = length // 2 # 절반

    total = 0
    for i in range(a, a + length):
        for j in range(b, b + length):
            if array[i][j] == 1:
                total += 1
    # 모두 0 이면 0, 모두1이면 length*length
    if total == 0:
        result[0] += 1
        return
    elif total == length*length:
        result[1] += 1
        return
    # 섞여있다면 4등분
    else:
        calculator(a, b, array, k) # 왼위
        calculator(a, b+k, array, k) # 왼아래
        calculator(a+k, b, array, k) # 오른위
        calculator(a+k, b+k, array, k) # 오른아래
    
# (0,0) 부터 data를 볼것인데 크기가 n이다
calculator(0, 0, data, n)
for i in result:
    print(i)
'''
1. 들어온 배열의 원소들이 모두 같은지 본다.
2. 배열의 모든값이 같지 않다면, 4부분으로 나눠 1번을 수행한다.
3. 1,2번 반복해서 모든 원소를 다 봤을 때, 0의개수, 1의개수를 출력해라

'''
# ##########################################
# ##########################################
# # 3/26 - 재귀인데 범위몰라서 그냥 때려넣기 
# n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)]

# result = [0] * 2 # [0]=흰, [1]=파

# def check(array):
#     global result
    
#     # total == count 이어야 됨?
#     length = len(array)
#     total = length*length 
    
#     # 1. 해당부분 배열의 값이 같은지 센다
#     pre = array[0][0]
#     # print(array, pre)
#     count = 0 
#     for i in range(length):
#         for j in range(length):
#             if array[i][j] == pre:
#                 count += 1
#     # 2. 다르다면 4등분해서 각각을 본다.
#     if count != total:
#         # 왼위
#         half_length = length // 2
#         tt = [[0] * half_length for _ in range(half_length)]
#         for i in range(half_length):
#             for j in range(half_length):
#                 tt[i][j] = array[i][j]
#         check(tt)
#         # 오른위
#         for i in range(half_length):
#             for j in range(half_length, length):
#                 tt[i][j-half_length] = array[i][j]
#         check(tt)
#         # 왼 아래
#         for i in range(half_length, length):
#             for j in range(half_length):
#                 tt[i-half_length][j] = array[i][j]
#         check(tt)
#         # 오른 아래
#         for i in range(half_length, length):
#             for j in range(half_length, length):
#                 tt[i-half_length][j-half_length] = array[i][j]
#         check(tt)
#     # 3. 같다면 값추가해주고 리턴
#     else:
#         result[pre] += 1
#         # print("카운트하나증가")
#         return

# check(data)
# # print(result)
# for i in result:
#     print(i)