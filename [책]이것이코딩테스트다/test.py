n = int(input())
coins = list(map(int, input().split()))
coins.sort()

# 돈을 만들 수 있는지 없는지
start = 1
for x in coins:
    if start < x:
        break
    start += x
    print(start)
print(start)

