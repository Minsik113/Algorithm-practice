##########################################
##########################################
# 추천하는 정답
# 필요한n만큼만 계산

n = int(input())

# 못생긴 수 담기위한 테이블
array = [0] * n 
array[0] = 1

# 2,3,5의 배수를 위한 인덱스
i2, i3, i5 = 0, 0, 0 # i2 = i3 = i5 = 0 가능

# 처음에 곱셈값을 초기화한다.
next2, next3, next5 = 2, 3, 5

# 1~n까지 못생긴 수 찾기
for k in range(1, n):
    # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
    array[k] = min(next2, next3, next5)
    # 인덱스에 따라서 곱셈 결과 증가
    if array[k] == next2:
        i2 += 1
        next2 = array[i2] * 2
    if array[k] == next3:
        i3 += 1
        next3 = array[i3] * 3
    if array[k] == next5:
        i5 += 1
        next5 = array[i5] * 5
# n 번째 수 출력
print(array[n-1])

##########################################
##########################################
# 내풀이 - set과 heapq이용
# n범위가 더 커지면 사용못한다.
'''
약수에 2,3,5 들어가면 리스트에 포함한다.

2배수 heapq에 넣음
3배수 heapq에 넣음
5배수 heapq에 넣음
n+1번째 pop한게 답 임
'''
import heapq

n = int(input())

h = []
heapq.heappush(h, 1)
# 이미 들어간 값인지 체크하기 위해
data = set()
data.add(1)
plus = [2,3,5]
for i in range(3):
    for j in range(1, 1000):
        temp = plus[i]*j
        if temp in data:
            continue
        else:
            heapq.heappush(h, temp)
            data.add(temp)
for i in range(n): # 
    print(heapq.heappop(h))
