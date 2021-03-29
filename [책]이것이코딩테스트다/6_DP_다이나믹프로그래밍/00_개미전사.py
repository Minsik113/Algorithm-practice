'''
dp테이블만든다 (3 ~ 100)
dp[i] = i번째에서 가장 많이 저장 할 수 있는 곡식 수
조건)
dp[i] = max(dp[i-2] + array[i],dp[i-1]) # 선택함 선택안함.
'''
# 처음풀이 - 이건 좀 직관적이다.
n = int(input())
array = list(map(int, input().split()))
dp = [0] * 101 # 100까지쓰기위해서
dp[0] = array[0]
dp[1] = max(array[0], array[1])

for i in range(2,n+1): # 2~n까지
    if i == n: # array인덱스는 n-1까지니까 마지막경우는 따로 빼주자.
        dp[i] = max(dp[i-2], dp[i-1])
    else:
        dp[i] = max(dp[i-2] + array[i], dp[i-1])
print(dp[n])

# 두번쨰 풀이
n = int(input())
array = list(map(int, input().split())) # 0~n-1 
dp = [0] * 101 # 100까지쓰기위해서
dp[0] = array[0]
dp[1] = max(array[0], array[1])

for i in range(2,n): # 2~n까지
    dp[i] = max(dp[i-2] + array[i], dp[i-1])
print(dp[n-1])