'''
가장 인접한 두 공유기 사이의 거리를 찾아보는것이다. = a라고하면

시작점 + a 가 가능한지보고
시작점 = 시작점+a로 바꿈
c <= 공유기설치 라면 범위늘려서 시행해본다. 최대거리를 출력

'''
n, c = map(int, input().split())
count = [0] * (200001) # 1~20만번째
for i in range(n):
    a = int(input())
    count[a] += 1
# 계차정렬한다
data = []
for i in range(1, 200001):
    while count[i] > 0:
        data.append(i)
        count[i] -= 1

# 예외처리 - 놓을 수 있는 공유기 수가 많다면 제일 거리차가짧은곳이 출력되어야하는데?


# 1. 놓을 수 있는거리를 1씩 증가시키면서 보자
start = 1 # 1 ~ 제일긴 거리로 놔볼것이다.
end = data[-1]-data[0] # 
max_value = 0

while start <= end:
    mid = (start + end) // 2 # 놓는 거리를 조정한다.
    pre = data[0] # 여기서 공유기 설치
    count = 1 # 공유기 세는 변수
    index = 1 # 집의 위치를 하나씩 이동할 변수

    # mid거리이상의 위치에 집이 있는지 체크
    while index <= len(data)-1:
        if data[index] - pre >= mid: 
            pre = pre + data[index] # 이전집위치 변경
            count += 1 # 공유기 1개 추가
        else:
            index += 1

    if count >= c: # 더 놓을 수 있다는 말이니까 범위 크기해서 본다
        start = mid + 1
        max_value = mid
        # print(mid,count, 'count>=c')
    else: # 더 못놓는다는 말이니까 범위 작게 해서 보자
        end = mid - 1
        # print(mid,count,'count<c')
print(max_value)
