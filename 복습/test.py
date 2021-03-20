from itertools import combinations

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
array = [i for i in range(n)]
min_value = int(1e9)
total = set()

for left in combinations(array, n//2):
    right = set()
    right = []
    for i in range(n):
        if i not in left:
            right.append(i)
    # 봤던거 안보기 위해서
    if left in total:
        break
    total.add(left)
    total.add(tuple(right))
    
    left = list(left)
    right = list(right)
    # left, right 합구하자
    l_sum, r_sum = 0, 0
    for i in range(len(left)):
        for j in range(len(right)):
            l_sum += data[left[i]][left[j]]
            r_sum += data[right[i]][right[j]]
    print(left, right, l_sum, r_sum)
    min_value = min(min_value, abs(l_sum - r_sum))
print()
print(min_value)