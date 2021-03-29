##########################################
##########################################
# 3/9 복습
'''
1. 전투력 높은 병사가 앞쪽.(내림차순 배치)
2. reverse해서 오름차순 배치하게 할까?
3. 최장 부분 수열 개수 구한다.
4. 전체수 - 3번 = 답

최장부분수열 O(N^2)
현재까지 봤던위치를 매번 다시보면서 최대 길이를 구한다.
dp[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
-> max(dp)구하면 최장 길이 나옴
'''

n = int(input())
array = list(map(int, input().split()))
array.reverse()

# dp생성
dp = [1] * n # 자기자신의 길이는 1이므로
# print(array)
# print(dp)
# LIS시작
for i in range(1, n): # i현재 j이전거
    for j in range(0, i):
        if array[i] > array[j]: # 현재 > 이전값 
            dp[i] = max(dp[j]+1, dp[i]) # (j위치의 최대길이+1, 현재값) 현재값 = 내가 제일 길다.
print(n-max(dp))

##########################################
##########################################
# 
'''
전형적인 dp아이디어인 LIS (가장 긴 증가하는 부분 수열)문제이다.
# 본 문제는 가장 긴 감소하는 부분 수열을 찾는 문제로 치환 가능하다.
# -> LIS 알고리즘을 조금 수정하여 적용하면 정답도출가능

# D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# 0 <= j < i 에 대하여, D[i] = max(D[i], D[j] + 1) if array[j] < array[i]
# -> 가장 긴 증가하는 부분 수열이니까  array[j] < array[i] 이다.
# => O(N^2)

# 이렇게 나온 D의 값은 우리가 만들 수 있는 증가하는 부분수열 중에서 가장 긴 수열의 길이가 저장되어있다.
# -> 병사 정보의 순서를 뒤집고, LIS적용하면됨
# '''
# n = int(input())
# array = list(map(int, input().split()))
# # 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
# array.reverse()

# # dp 초기화
# dp [1] * n
# # LIS수행
# for i in range(1, n):
#     for j in range(0, i):
#         if array[j] > array[i]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(n - max(dp))

# '''
# array리스트에 전투력 저장
# dp[i] = [i번째까지 최대 병사 수의 합, ]

# n = 2000이니 n^2 = 4백만. 충분하다.
# if array[i] > array[i-1]: # 전투력이 작은 병사 나오면 더한다.
#     dp[i] = dp[i-1] + array[i][1]
# else: # 전투력이 큰 애가 나온다면? 
#     # i에서 거꾸로 올라가며 array[i][1]보다 큰 값이 나오는 index를 찾는다.
#     index = 0
#     for j in range(i,-1): # i~0위치까지
#         if array[j][1] > array[i][1]:
#             index = j
#             break
#     # 더 큰 수가 끝까지 안보일 수도 있다. 이럴경우는 현재값과 이전의 제일큰 dp값과 비교해서 
#     # 현재값이 더 크다면 현재값넣고, 이전dp중 현재값보다 큰게있다면 현재값을 뺀다.?
#     dp[i] = dp[j] + array[i][1]

# '''

# n = int(input())
# array = list(map(int, input().split()))
# dp = [0] * (n) # dp[i] = i번째까지 큰 병사들의 수
# num = [0] * (n) # dp[i]를 이루기 위해 더해진 병사 수

# # dp시작
# dp[0] = array[0]
# num[0] = 1
# for i in range(1,n):
#     # print('작은게나왔자낭',array[i-1],array[i],'라서',end=' ')
#     # 1번. 더 작은게 나오면 일단 더함
#     if array[i] < array[i-1]: 
#         # print('i가 더 작은곳 들어옴')        
#         dp[i] = dp[i-1] + array[i]
#         num[i] = num[i-1] + 1
#     # 2번. 더 큰 병사수를 가진애가 나오면
#     elif array[i] > array[i-1]: 
#         # print('i가 더 큰곳 들어옴', end=' ')
#         # 더 큰 병사 수를 가진애가 나오면 현재병사수보다 큰 애를 찾는다
#         # i위치부터 0까지 거꾸로 찾는다.
#         index = 0
#         flag = False # 더 큰애 발견했는지 체크 하기 위해
#         for j in range(i-1,-1,-1):
#             # print(j,array[j],array[i])
#             if array[j] > array[i]: # 자기보다 큰값을 가진 애를 발견하면 나온다
#                 flag = True
#                 index = j
#                 break
#         # print(index,'위치 값은',array[index])
#         # 큰애를 발견했다면, 지금까지 병사수와 dp[index]+현재값비교
#         if flag:
#             if dp[i-1] > dp[index] + array[i]: # 2-1. 현재들어온애보다 이전들의합이 더 크다면 뺴야지
#                 dp[i] = dp[i-1]
#                 num[i] = num[i-1]
#             elif dp[i-1] < dp[index] + array[i]: # 2-2. 이전 병사들의 합보다 현재들어와서 더 커졋다면 이거로 대체
#                 dp[i] = dp[index] + array[i]
#                 num[i] = num[index] + 1
#         # 큰애 발견 못했다면, 현재값과 지금까지 제일큰 수랑 누가 더 큰지 비교해야함
#         else:
#             if array[i] > dp[i-1]:
#                 dp[i] = array[i]
#                 num[i] = 1
#             else:
#                 dp[i] = num[i-1]
#                 num[i] = num[i-1]
#     # 3번. 병사수 같다면? 이전꺼 그대로 옮김            
#     else: 
#         # print('값이 같네 들어옴')
#         dp[i] = dp[i-1]
#         num[i] = num[i-1]
# #     print(dp)
# #     print(num)
# # print()    
# # print(dp)
# # print(num)
# print(n-num[n-1])

