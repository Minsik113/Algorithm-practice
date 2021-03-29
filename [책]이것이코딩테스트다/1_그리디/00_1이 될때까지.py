'''
그리디
1. 나눌 수 있으면 나누는게 제일 좋다.
2. 나눴다면 나눈수를 가지고 계산에 들어가라
'''
##########################################
##########################################
# N이 100억 이상의 큰 수에도 빠르게 동작하게하려면
# N이 K의 배수가 되도록 효율적으로 한번에 뺴는 방식으로 짜보자.
# O(log)시간이 걸림.
n, k = map(int, input().split())
result = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 -1하기
    target = (n//k) * k # k로 나눌 수 있는 n이하의 가장 가까운 수
    result += (n - target) # -1을 얼마나 해야 target이 나오는지 
    n = target
    if n < k:
        break
    
    # k로 나누기
    result += 1
    n //= k

result += (n-1)
print(result)

##########################################
##########################################
# 단순한 방법
# n, k = map(int, input().split())
# num = n
# count = 0
# if k == 1:
#     print(n-1)
#     exit()
# # N이 K이상이라면 K로 나누기
# while True:
#     if num == 1:
#         print(count)
#         break
#     if num % k == 0: # 
#         num = num // k
#         count += 1
#     else:
#         num -= 1
#         count += 1
    
