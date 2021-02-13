'''
O(N+K)
1. N이 100만아래면 용이하게 사용가능
2. 제일큰수와 가장 작은수가 차이가 작으면 좋다.
-> 배열을 N까지 선언하고 개수를 세기 때문이다.
'''
array = [1,5,2,7,4,10,9,2,1,0,6,8,9,14]
count = [0] * ((max(array)+1))

for i in range(len(array)):
    count[array[i]] += 1

# 1-몇개 2-몇개
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')


