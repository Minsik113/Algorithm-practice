# 1/20
# 입력: k, n
# 내용: 
#  k개의 길이의 랜선들을 입력받고, n개 만큼 자를것이다.
# 자를 수 있는 최대길이는? 단 n개이상으로 자르는것도 괜찮음.
# 출력: 최대길이

# 10^4 10^6 O(NM)은 안됨. O(NlogM)으로.

#################  ################
k, n = map(int,input().split(' ')) # 가지고 있는 랜선 개수,  필요한 랜선 개수
array = [int(input()) for _ in range(k)]
array.sort()

 # 기준은 랜선의 길이
start = 1 # 작은거부터 증가하는식으로 해야하니까 1임
end = array[-1] # max가 제일 긴 길이니까.
result = 0

while start <= end:
    mid = (start + end) // 2
    lans_sum = 0

    for i in array:
        if i // mid: # 나눠진다면
            lans_sum += (i // mid)
    
    if lans_sum >= n: # 좀더 크게 길이를 잘라보자
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)

#################  ################
k, n = map(int, input().split(' '))
array = [int(input()) for _ in range(k)]
array.sort()

start = 1
end = array[-1]
result = 0
while start <= end:
    # 몇 cm의 크기로 잘라낼 것인가
    mid = (start + end) // 2
    # 해당 크기로 잘라냈을 때 몇개의 랜선이 생기는가
    lines = sum([(i // mid) for i in array])

    # 잘라낸 개수가 기준보다 많다면, 더 큰 단위로 잘라서 개수를 줄여도된다.
    if lines >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)
        
    

