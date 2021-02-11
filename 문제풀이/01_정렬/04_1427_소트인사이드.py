# 1/15
# 문제 유형: 정렬, 배열
# 추천 풀이 시간: 25분

# 1~N~10^9

n = input()
data = []

for i in range(0,len(n)):
    data.append(n[i])

data.sort(reverse=True)

print(''.join(data)) # list -> str 로 바꿈

#########################
# sys.stdin.readline사용
#########################
import sys

test = list(sys.stdin.readline().rstrip())

test.sort(reverse=True)

print(''.join(test))

# 동빈나

array = input()
for i in range(9,-1,-1): # 9부터 0까지 볼거다. 
    for j in array:
        if int(j) == i:
            print(i,end='')
