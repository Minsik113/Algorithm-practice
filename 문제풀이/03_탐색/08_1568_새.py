# 1/19
# 문제 난이도: Bronze 4
# 문제 유형: 탐색
# 추천 풀이 시간: 20분

# N이 최대 1,000,000,000
# k가 반복적으로 증가하므로, 날아가는 새의 마리 수는 빠르게 증가한다. O(n^2)
# 다라서 요구하는대로 단순히 구현하여 정답 처리를 받을 수 있다.
# 등차수열의 시간복잡도는 O(n^2)임. n^2이 1,000,000,000개이므로 사실상 대략 O(루트n)이다.

###################  ###################
n = int(input())
k = 1
count = 0

while n > 0: # 0 보다 작은경우는 if문에 걸려서 나올수 없다.
    if n < k:
        k = 1
    
    n -= k
    k += 1
    count += 1
print(count)

###################  ###################
n = int(input())
number = 1
count = 0

while True:
    if n == 0: # 날아갈 새가 없다
        print(count)
        break
    elif n < number: 
        number = 1
    else: # 새들이 날아갈때
        n -= number # n = 13 
        count += 1 # count = 2
        number += 1 # number = 2
        
##################  ####################
# 동빈나

n = int(input())
result = 0
k = 1

while n != 0: # 모든 새가 날아갈 때까지
    if k > n:
        k = 1
    n -= k
    k += 1
    result += 1
print(result)


