# 4/23
import bisect, sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

d = [data[0]]

for i in range(1, n):
    # 지금나온게 저장된 리스트의 제일 큰 값보다 크면 이어붙인다
    if data[i] > d[-1]:
        d.append(data[i]) 
    else:
        idx = bisect.bisect_left(d, data[i])
        d[idx] = data[i]

print(len(d))