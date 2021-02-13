'''
dp[i] = i에 놓았을때 거리차이
제일작은i출력
'''


# 시간초과
n = int(input())
array = list(map(int, input().split()))
dp = [] # 최대 20만

for house in array:
    total = 0
    for j in range(len(array)):
        total += abs(house - array[j])
    dp.append((house,total)) # 여기설치하면,비용
answer = sorted(dp, key=lambda x:x[1])
print(answer[0][0])

