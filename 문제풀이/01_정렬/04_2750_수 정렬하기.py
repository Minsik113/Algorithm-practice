# 1/15
# 문제유형: 정렬
# 추천 풀이 시간: 15분

# 4~
# 1~N~1000이니까 2중 for문해도 10^6임

################################################
# 선택정렬 알고리즘 O(n^2)
# 매번 제일 작은 수 or 제일 큰 수 골라서 하나씩 배열
################################################
data = []

x = int(input())
for i in range(0,x):
    data.append(int(input()))

for i in range(0, len(data)-1):
    min = i
    for k in range(i+1, len(data)):
        if data[min] > data[k]:
            min = k
    # 제일작은게 min임.
    data[i], data[min] = data[min], data[i]

for i in data:
    print(i)

##################################################
# 내부 알고리즘 O(NlogN) - sys.stdin.readline()사용
# 리스트.sort()
##################################################
x = int(sys.stdin.readline())
data = []

for _ in range(x):
    data.append(int(sys.stdin.readline()))

data.sort()

for i in data:
    print(i)

#################################################
# 내부 알고리즘 O(NlogN) - input() 사용
# 리스트.sort()
#################################################
n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array.sort()
for i in array:
    print(i)

    import sys

#################################################
# 계수정렬 O(N) - 힘드네
# 이렇게는 안풀듯
#################################################
import sys

data = [0] * 2001 # -1000 ~ 1000 = 2001개
n = int(sys.stdin.readline())

for _ in range(n):
    k = int(sys.stdin.readline())
    if k > 0:
        data[1000+k] += 1
    else: # 음수
        data[abs(k)] -= 1

for i in range(1000,-1,-1):# 오름차순이니 음수는 거꾸로 봐야함
    if data[i] != 0:
        for _ in range(abs(data[i])):
                print(-i)

for i in range(1001, 2001): # -1000 ~ 0 ~ 1000 . 2000개
    if data[i] != 0:
        for _ in range(data[i]):
            print(i-1000)

    
            
        


