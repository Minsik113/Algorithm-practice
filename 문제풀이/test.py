'''
무게 : 1~10
1보다 큰 볼링공 개수: dp[1] = n-sum(1)
2보다 큰 볼링공 개수: dp[2] = dp[1]-sum(2)
'''
n, m = map(int, input().split())
array = list(map(int, input().split()))

data = [0] * (m+1) # 무게가 1~10까지
for i in array:
    data[i] += 1

result = 0
for i in range(1, m+1):
    target = data[i]
    n = n - target
    result += target
print(result)



