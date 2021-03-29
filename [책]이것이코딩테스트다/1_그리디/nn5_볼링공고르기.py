'''
1~N번 까지 볼링공이있음
1. 무게가 1일때 고를 수 있는 경우 + 무게가 2일때 고를 수 있는 경우 ... 
2. 무게가 m까지 1번 반복

● 조합으로 풀면 안됨
1000C10만 해도 263409560461970212832400 임

풀이 1) O(n^2)
n = 10^3 임
1. N^2 = 10^6 충분.
2. a보다 무게 큰거 나올 때마다 더해준다.

풀이 2) O(n + m)

'''

##########################################
##########################################
# 3/16 O(N^2)하면 충분하게 풀 수는 있다. 아래보다 느림
n, m = map(int, input().split())
data = list(map(int, input().split()))

count = 0
for i in range(n):
    for j in range(n):
        if i == j :
            continue
        if data[i] < data[j]:
            count += 1
print(count)

##########################################
##########################################
# O(N)으로 빠르게 풀 수 있다.
n, m = map(int, input().split())
data = list(map(int, input().split()))
check = [0] * (m+1)

# 1~m까지 볼링공이 몇개씩 들어있는지 체크
for i in data:
    check[i] += 1

result = 0
for i in range(1,m+1):
    n -= check[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += check[i] * n # B가 선택하는 경우의 수와 곱한다.
print(result)





