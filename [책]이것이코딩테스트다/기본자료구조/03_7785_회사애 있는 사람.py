
## 내가품
import sys

x = int(sys.stdin.readline())
data = dict()

for _ in range(x):
    a, b = sys.stdin.readline().rstrip().split(' ')
    
    if b == 'enter':
        data[a] = b
    else:
        data[a] = 0

l_data = []
for i in data:
    if data[i]:
        l_data.append(i)

l_data.sort(reverse=True)
for i in l_data:
    print(i)

# 다른 블로그
import sys

x = int(sys.stdin.readline())
data = dict()

for _ in range(x):
    a, b = sys.stdin.readline().rstrip().split(' ')
    
    if b == 'enter':
        data[a] = 1
    else:
        del data[a]

s = sorted(data.keys(),reverse=True)

for i in s:
    print(i)
