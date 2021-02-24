'''
완전탐색 -> 값 찾기?
N=10^3이다. 
풀이1. 앞에서부터 나오는 수 체크 
풀이2. 나올 수 있는 모든 조합 체크  - 내풀이

풀이1)
data.sort()
target = 1
for x in data:
    if target < x 라면 끝
    else target += x

target += x 란 target이 3이라면 1,2,3동전이 있다는 뜻으로 
1~5까지 만들 수 있으므로 target=6으로 바꾸라 라는 의미

'''
##########################################
##########################################
# 다시풀기
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# target = 1
# for x in data:
#     # 만들 수 없는 금액
#     if target < x:
#         break
#     target += x
    
# print(target)

##########################################
##########################################
# 조합으로 풀음. 시간안에 안되려나? -> n = 1000까지임. 안됨. 100C50 만 해도 못품.
# nC1 + ... nCn
# from itertools import combinations

# n = int(input())
# array = list(map(int, input().split()))
# result = set()
# for i in range(1,n+1):
#     for j in combinations(array,i):
#         sub_sum = sum(j)
#         result.add(sub_sum)
# # print(result)
# count = 1
# while True:
#     if count in result:
#         count += 1
#     else:
#         print(count)
#         break
