'''
중간값출력하면됨
-> 나는 min,max의 중간값을 찾아서 왼쪽 오른쪽순으로비교
 => 시간초과;
-> 가장 중간값출력
'''
##########################################
##########################################
# 중간값출력하면됨
n = int(input())
array = list(map(int, input().split()))
array.sort()

print(array[(n-1) // 2])

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

