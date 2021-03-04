'''
집 리스트의 중간값 출력하면됨
-> 가장 중간값출력
'''
##########################################
##########################################
# 중간값출력하면됨
n = int(input())
array = list(map(int, input().split()))

array.sort()
print(array[len(array)//2 - 1])
##########################################
##########################################
# 시간초과

# n = int(input())
# array = list(map(int, input().split()))
# dp = [] # 최대 20만

# for house in array:
#     total = 0
#     for j in range(len(array)):
#         total += abs(house - array[j])
#     dp.append((house,total)) # 여기설치하면,비용
# answer = sorted(dp, key=lambda x:x[1])
# print(answer[0][0])

