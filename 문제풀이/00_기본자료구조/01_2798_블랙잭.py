# 1/11 2798-블랙잭  
'''
파이썬은 1초에 2천만의 경우를 계산함.
전체 경우의 수를 다 계산해도 백만 이라서 금방끝남.
N장뽑고 3장의 카드합 <= M 중 제일 가까운것 골라라.
'''
n, m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

# 다 계산해도 된다.
answer = 0
length = len(data)

for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= m:
                answer = max(sum_value, answer)
print(answer)            

# 나동빈
n,m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

result = 0

for i in range(0, len(data)):
    for j in range(i+1, len(data)):
        for k in range(j+1, len(data)):
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= m:
                result = max(result, sum_value)
                
print(result)