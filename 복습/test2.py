import sys
input = sys.stdin.readline 

n, c = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()

# 예외처리 - 제일짧은 거리를 출력해줘야한다
if n <= c:
    pre = data[0]
    min_value = int(1e9)
    for i in range(1, len(data)):
        min_value = min(min_value, data[i]-pre)
        pre = data[i]
    print(min_value)
    exit()

# 거리로 접근하자    
start = 1 # 제일짧은 거리차이는 1일것이지
end = data[-1] - data[0] # 제일 긴 거리차이 
max_value = 0

while start <= end:
    mid = (start + end) // 2
    count = 1 # 시작위치에는 공유기 1개 설치하기때문에
    pre = data[0] # 시작위치부터 mid 씩보면서 거리에 집이 있는지 체크
    # 맨 끝까지 놔본다
    for i in range(1, len(data)):
        if data[i] - pre >= mid:
            count += 1
            pre = data[i]
            if count == c:
                break
    
    if count == c: # 설치가능하면 길이 좀 늘려보자
        max_value = mid
        start = mid + 1
    else: 
        end = mid - 1
print(max_value)

