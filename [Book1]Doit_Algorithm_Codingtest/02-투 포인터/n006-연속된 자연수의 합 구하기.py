'''
날짜: 2022.09.30
시간복잡도: O(N)

문제: https://www.acmicpc.net/problem/2018
풀이방식:

n = 1000만임.  O(N)

투포인트
'''
from tracemalloc import start


n = int(input())
start_index = 1
end_index = 1
cnt = 1
total = 1

while end_index != n:
    # 같으면
    if total == n:
        cnt += 1
        end_index += 1
        total += end_index
    # 총합이 크면 start를 당겨와야함
    elif total > n:
        total -= start_index
        start_index += 1
    # 총합이 작으면 end를 늘려야함
    else:
        end_index += 1
        total += end_index
print(cnt)
        


