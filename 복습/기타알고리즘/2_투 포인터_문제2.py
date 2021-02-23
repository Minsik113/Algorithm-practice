'''
병합정렬할때 느낌이다.
'''

n, m = 4, 5
a = [1,4,6,10]
b = [2,3,5,8,9]

result = [0] * (n+m)
i = 0
j = 0
k = 0

# 모든 원소가 리스트에 담길 때까지 반복
while i < n or j < m:
    # 리스트 B의 모든 원소가 처리 or 리스트 A의 원소가 더 적을 때
    if j >= m or (i < n and a[i] <= b[j]):
        # 리스트 A의 원소를 결과 리스트에 옮긴다.
        result[k] = a[i]
        i += 1
    # 리스트 A의 모든 원소가 처리 or 리스트 B의 원소가 더 적을 때
    else:
        result[k] = b[j]
        j += 1
    k += 1

for i in result:
    print(i, end=' ')
    