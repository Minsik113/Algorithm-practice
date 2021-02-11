'''
1/20
내용: 서로 다른 N개의 자연수의 합이 S라고 한다. 
    S를 알 때, 자연수 N의 최댓값은 얼마일까?
입력: S
출력: N의 최댓값
'''
# O(N) 으로하면 10^9니까 시간안에못함
# O(루트N) = 앞에서부터 다 더하면 이렇게나옴
# or O(logN)으로하자.

##################  ##################
# O(루트S)
s = int(input())
i = 0
sum_number = 0

while i + sum_number < s:
    i += 1
    sum_number += i
print(i)

##################  ##################
# O(lonS)
n = int(input())

start = 0
end = n
answer = 0

while start <= end:
    mid = (start + end) // 2
    
    if mid * (mid + 1) // 2 <= n:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)        

