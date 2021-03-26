# '''
# 이항정리
# (n) = n! / k!(n-k)!
# (k)
# 단순히 배열에 넣어서하면 '메모리초과'

# -> 1. 페르마의 소정리
# -> 2. 확장 유클리드 호제법

# '''
# ##########################################
# ##########################################
# # 메모리초과;
# n, k = map(int, input().split())
# result = [0] * (n+1) # 1~n까지의 factorial 값을 저장
# result[1] = 1

# # n까지의 factorial값을 구한다
# for i in range(2, n+1):
#     if result[i] == 0:
#         result[i] = i * result[i-1]

# print(int(result[n] / (result[k]*result[n-k])) % 1000000007)