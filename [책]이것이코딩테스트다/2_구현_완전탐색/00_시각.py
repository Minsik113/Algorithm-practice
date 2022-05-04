'''
완전탐색 

24, 60 60 이므로 전체 다 계산해도 84000개뿐이다.
-> 굉장히 짧은 시간이 걸림. 전부다보자 3중포문.
brute force

'''
##############
# 2022/04/30 #
##############
# 시 분 초 나눠서 계산
n = int(input())
count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1
print(count)


# n = int(input())
# count = 0
# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i)+str(j)+str(k):
#                 count += 1

# print(count)
