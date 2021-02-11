test = int(input())
for _ in range(test):
    index = int(input()) # 여기까지 테이블 만들어야함.
    if index == 0:
        print('1 0')
    elif index == 1:
        print('0 1')
    else:
        dp = [] # 0 ~ 40
        dp.append((1,0))
        dp.append((0,1))
        for i in range(2,index+1):
            pa, pb = dp[i-2]
            a, b = dp[i-1]
            dp.append((pa+a,pb+b))
        print(dp[index][0], dp[index][1])
    # print(' '.join(map(str,dp[index])))
    print(dp)
