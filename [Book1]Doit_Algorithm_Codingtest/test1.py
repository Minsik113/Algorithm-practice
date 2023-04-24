'''
왜 도대체 뭐가잘못된걸까

'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
s = [0]
temp = 0 

# 부분합
for i in arr:
    temp = temp+i
    s.append(temp)

for _ in range(m):
    a, b = map(int, input().split())
    print(s[b]-s[a-1])