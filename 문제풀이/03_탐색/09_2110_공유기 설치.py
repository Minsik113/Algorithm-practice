# 1/20
# 문제 난이도: Silver 1
# 문제 유형: 이진 탐색
# 추천 풀이 시간: 40분

# N은 최대 200,000이며 집의좌표는1,000,000,000이다.
# 이진 탐색을 이용하여 O(N * logX)에 문제를 해결할 수 있다.

# 데이터의 값이 매우 크거나 데이터의 개수가 매우 큰 경우에는 이진탐색을 고려해봐라
# 매우 값이 큼에도 탐색을 해야한다면, 이진탐색을 해보자.
# O(x)이어도 10억이니까 O(logX)나 O(루트x)를 이용하라는 의미이다.

# 20만 x logX = 20만 x 30 = 600만
# 가장 인접한 두 공유기 사이의 최대 Gap을 이진 탐색으로 찾는다.

####################  ####################

n, c = map(int, input().split())
array = []

for _ in range(n):
    array.append(int(input()))

array.sort()

start = 1 # 두 공유기사이의 거리를 점점 바꿔갈것이다.
end = array[-1]
result = 0

while start <= end:
    mid = (start + end) // 2
    value = array[0]
    count = 1
    
    for i in range(len(array)):
        if array[i] >= value + mid: #
            count += 1
            value = array[i]
            if count >= c:
                break

    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)

