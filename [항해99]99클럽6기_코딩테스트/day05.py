'''
날짜: 2025.04.04
링크: https://hanghae99.spartacodingclub.kr/99club/lms
시간복잡도: O(N)

1.학습키워드
구현 -> 구간합

2.문제
연속된 k개씩봐가면서 최대값을 적어라. N이 10만까지라 NlogN이하로.
부분합 구하는 방법을 알아야 풀 수 있다.
    응용)각각의 항을 연속적인 N개로 센 후, 그 합을 적어라.
    N개를 연속으로 볼 때 합 30, N+1개를 연속으로 볼 때 합25 ...

3.어떤 문제가 있었고, 나는 어떤 시도를 했는지
1~n사이의 수중 연속될 수 있는건 1~n-1개씩 볼 때 겠지? 모든경우를 담을 리스트만들어서 넣으면될듯? X
부분합 구하는 방법을 알아야 풀 수 있다.

4.어떻게 해결했는지
부분합 구하는 방법을 알아야 풀 수 있다.

5.무엇을 새롭게 알았는지
-그냥 돌리면 O(N^2)로 시간초과
-처음본게 마이너스면 넘기기. 시간초과 어찌됐던 O(N^2)
-부분합 O(N)

#99클럽 #TIL #개발자취업 #코딩테스트준비 #코테연습 #항해99 #코테

'''

# 1.변수선언
n, k = map(int,input().split())
nums = list(map(int, input().split()))
prefix_sum = [0] * (n+1)

a = -999
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + nums[i]
#print(prefix_sum)    

for i in range(n-k+1):
    #print(prefix_sum[i+k] - prefix_sum[i])
    a = max(a, (prefix_sum[i+k] - prefix_sum[i]))
    
print(a)


#######
# 응용) k가 주어지지않았을때, i번째에서 연속된x개의 합 중 최대값 저장하기
#######
#result = []
#for x in range(1, n):  # 연속으로 볼 개수 1 ~ n-1개.
#    maxnum = -999 # 수는 -100~100까지가능이므로 0으로하면 안됨.
#    for i in range(n):
#        temp = 0 
#        for j in range(i,i+x): # i부터 연속된x개의 합을 temp에 저장한다
#            if j >= n:
#                break
#            temp += nums[j]
#        maxnum = max(maxnum, temp)
#    result.append(maxnum)
#print(result)

