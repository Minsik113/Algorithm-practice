N, M, K = map(int, input().split())
array = list(map(int, input().split()))
array.sort(reverse=True)
max_value = array[0] 
next_value = array[1]

# 가장 큰 수가 더해지는 횟수 계산
count = (M // (K+1)) * K # 큰수k번+다음수1번의 총 횟수
print(count)
count += M % (K+1) # 쩌리 횟수

print(count)
result = 0
result += count * max_value #가장큰 수만큼 더함.
print(result)
result += (M-count) * next_value
print(result)

############