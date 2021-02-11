'''
# 1/31
# 문제 난이도: Gold 5
# 문제 유형: 그리디
# 추천 풀이 시간: 40분

'''
import heapq

n, m = map(int, input().split())
array = list(map(int, input().split()))

right = []
left = []

dif = max(max(array), -min(array)) # 양음 중 제일 큰 값

for i in array: 
    if i > 0: # 최대힙으로 저장되어있음
        heapq.heappush(right, -i) # 빼면 제일 큰 수
    else: # 최소힙으로 되어있으나 음수여서
        heapq.heappush(left, i) # 뺴면 제일 큰 수가 나옴

# print(right)
# print(left)
result = 0

# right 쪽에 관하여 탐색
while right:
    if len(right) >= m:
        result += heapq.heappop(right)*2
        for _ in range(m-1):
            heapq.heappop(right)
    else:
        result += heapq.heappop(right)*2
        while right:
            heapq.heappop(right)

# left 쪽에 관하여 탐색        
while left:
    if len(left) >= m:
        result += heapq.heappop(left)*2
        for _ in range(m-1):
            heapq.heappop(left)
    else:
        result += heapq.heappop(left)*2
        while left:
            heapq.heappop(left)
print(abs(result)-abs(dif))

##############  ##############
# 다시풀음
import heapq

n, m = map(int, input().split())
array = list(map(int, input().split()))

max_value = max( max(array),-min(array) )
        
left = []
right = []

for i in array:
    if i > 0:
        heapq.heappush(right, -i)
    else:
        heapq.heappush(left, i)
# 제일 큰 값이 제일 먼저 출력됨.

result = 0

while right:
    result += heapq.heappop(right)
    for _ in range(m-1):
        while right:
            heapq.heappop(right)

while left:
    result += heapq.heappop(left)
    for _ in range(m-1):
        while left:
            heapq.heappop(left)
print(-(result*2) - max_value )
    

# while left:
#     if len(left) >= m:
#         result += heapq.heappop(left)
#         for i in range(m-1):
#             heapq.heappop(left)
#     else:
#         result += heapq.heappop(left)
#         while left:
#             heapq.heappop(left)

##############  ##############
# 나동빈
import heapq
# 최대값 가지고 할거니까 max heap으로쓰자.

n, m = map(int, input().split())
data = list(map(int, input().split()))

positive = []
negative = []
largest = max(max(data), -min(data)) # 양음중 제일 큰 값
for i in data:
    if i > 0:
        # 양수면 -를 해줘서 heapq에 넣어준다. 제일 큰수가 제일 작은수가 됨
        heapq.heappush(positive, -i) # max-heap이됨.
    else: 
        # 음수면 절대값한다면 제일 큰수가 제일 작은수가 됨.
        heapq.heappush(negative, i) # 

result = 0

while positive:
    result += heapq.heappop(positive)
    for _ in range(m-1):
        if positive:
            heapq.heappop(positive)

while negative:
    result += heapq.heappop(negative)
    for _ in range(m-1):
        if negative:
            heapq.heappop(negative)

print(-result*2 - largest)



