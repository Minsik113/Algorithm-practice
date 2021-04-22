'''
동빈나 그리디
1. 오름차순 정렬
2. 0번 k번반복 
3. 1번 1번
4. 2~3번의 횟수가 m이 될때까지 반복
5. 그 합을 출력
'''
##########################################
##########################################
# 
N, M, K = map(int, input().split())
array = list(map(int, input().split()))
array.sort(reverse=True)
max_value = array[0] 
next_value = array[1]

# 가장 큰 수가 더해지는 횟수 계산
count = (M // (K+1)) * K # 큰수k번+다음수1번의 총 횟수
count += M % (K+1) # 쩌리 횟수
# count*큰수 = 큰수들어가는횟수
# M-count = 2번째큰수 들어가는 수 하면 됨.
result = 0
result += count * max_value 
result += (M-count) * next_value
print(result)

##########################################
##########################################
# 단순한 풀이 - 수가 커지면 적용X
N, M, K = map(int, input().split())
array = list(map(int, input().split()))
array.sort(reverse=True)
# print(array)
count = M
max_value = array[0]
next_value = array[1]
result = 0

while count > 0: # m번 더할것이다.
    if count >= K: # m이 k보다 크면 k번 보면됨
        result += max_value * K
        count -= K
    else:
        for _ in range(K):
            result += max_value
            print(result)
            exit()
    if count >= 1: 
        result += next_value
        count -= 1
print(result)
