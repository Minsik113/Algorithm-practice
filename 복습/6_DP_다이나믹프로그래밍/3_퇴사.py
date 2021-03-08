'''
d[i] = i번째 날부터 마지막 날까지 낼 수 있는 최대 이익

'''
n = int(input())
t = []
p = []
dp = [0] * (n+1) 
max_value = 0 

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

# 리스트를 거꾸로 확인
for i in range(n-1,-1,-1):
    time = t[i] + i
    # 상담 기간 안에 끝나는 경우
    if time <= n:
        # 현재까지의 최고 이익 계산
        dp[i] = max(max_value, p[i] + dp[time])
        max_value = dp[i]
    # 기간 벗어나는 경우
    else:
        dp[i] = max_value
print(dp)


