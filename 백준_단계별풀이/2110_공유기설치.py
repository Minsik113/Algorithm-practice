# 3/27
'''
집에 공유기 설치
가장 인접한 공유기 사이의 거리가 최대가 되게해라.
거리가 1 2 ... 마다 공유기설치한다
-> 현재집~다음집과의 거리가 mid 보다 작다면 다음집을본다.

이진탐색으로 비교할 거리를 정함.
'''
import sys
input = sys.stdin.readline
# n개의집에 c개공유기 설치하고싶음
n, c = map(int, input().split())
data = [int(input()) for _ in range(n)]
data.sort()

# 제일짧은거리는 1이겠고
# 제일긴거리는 max(data) - min(data)
start = 1
end = data[-1] - data[0]
max_value = 0

while start <= end:
    mid = (start + end) // 2
    count = 1 # 0번째집에는 설치
    
    # 최소 mid의 길이 마다 공유기 설치해보자
    pre = data[0]
    for i in range(1, len(data)):
        dif = data[i] - pre
        # 차이가 mid이상이라면 설치함
        if dif >= mid:
            pre = data[i]
            count += 1
            if count == c:
                break
    if count == c:
        start = mid + 1
        max_value = mid
    elif count < c:
        end = mid - 1

print(max_value)