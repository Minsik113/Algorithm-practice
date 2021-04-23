import bisect
n = int(input())
a = list(map(int, input().split()))

q = []
temp = []
for i in range(n):
    if not q or q[-1] < a[i]:
        q.append(a[i])
        temp.append( (len(q)-1, a[i]) )
    else:
        q[bisect.bisect_left(q, a[i])] = a[i]
        temp.append(( bisect.bisect_left(q, a[i]), a[i] ))
print(q)
print(temp)

result = []
last_idx = len(q) - 1
for i in range(len(temp)-1, -1, -1):
    if temp[i][0] == last_idx:
        result.append(temp[i][1])
        last_idx -= 1
print(len(result))
print(*reversed(result))