# '''
# 공유기를 집에 설치한다.
# 가장 가깝게 붙어있는 공유기사이의 거리가 최대값이 나올 수 있게 하라.
# (양 사이드는 무조건 설치.)

# 공유기 사이의 최대 거리니까 
# 최대거리를 바꿔가면서 공유기 최대 설치 대수를 볼까?
# -> 매 순간 실제로 공유기를 설치하여 C보다 많은 개수로 공유기를 설치할 수 있는지 체크하자.
# -> 가장 인접한 공유기 사이의 최대거리를 하나씩 증가시키면서 체크
# '''
# n, c = map(int, input().split())
# array = []
# for i in range(n):
#     array.append(int(input()))
# array.sort()

# start = array[1] - array[0] # 집의 좌표중 가장 작은 값?
# end = array[-1] - array[0] # 집의 좌표중에 가장 큰 값?

# while start <= end:
#     mid = (start + end) // 2 # 가장 인접한 두 공유기 사이의 거리(gap)
#     value = array[0]
#     # mid값을 이용해 공유기 설치
#     for i in range(1, n): # 앞부터 차례대로 설치
#         if array[i] >= value + mid:
#             count += 1
#             value = array[i]
#     if count >= c: # C개이상의 공유기 설치됨. 거리를 늘려보자
#         start = mid + 1
#         result = mid
#     else:
#         end = mid - 1

# print(result)