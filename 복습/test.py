'''
집에 공유기설치한다. 공유기가 C개 설치.
가장 가까운 공유기 사이의 거리가 최대로 해야함

1. 집마다 거리 1~제일긴거리 이 사이로 공유기 설치한다.
2. 공유기를 C개 이상 설치할 수 있다면 거리 늘려봄
3. 공유기를 C개 보다 작게 설치할 수 있다면 거리 줄여봄
'''
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
array = [int(input()) for _ in range(n)]
array.sort() # 20만 x 약15 = 300만

# 예외처리
if c >= n: # 공유기 대수가 더 많으면 가장 인접한애 거리 출력한다.
    min_value = int(1e9)
    prev = array[0]
    for i in range(1, len(array)):
        min_value = min(min_value, array[i] - prev)
        prev = array[i]
    print(min_value)
    exit(0)

# 거리로 접근 할 것이다.
start = 1 # 제일짧은거리
end = array[-1] - array[0]

result = 0
while start <= end:
    mid = (start + end) // 2 # mid마다 공유기 설치

    # 1번. 첫 집부터 끝집까지 mid이상위치에 공유기 설치
    prev = array[0]
    count = 1 # 설치한 공유기 개수를 셀 변수 (0번째집에는 설치)
    for i in range(1,len(array)):
        if array[i] - prev >= mid: # 공유기 설치할 수 있는 집 발견
            prev = array[i] # 현재 위치 바꿈
            count += 1
            if count == c: # 더 안봐도됨
                break

    # 2번. mid길이로 다 설치했을 때 설치한 공유기 대수를 확인
    if count == c: # 더 설치할 수 있다면 길이 늘려봄
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)


