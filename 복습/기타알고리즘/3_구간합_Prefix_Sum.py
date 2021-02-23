n = 5
data = [10,20,30,40,50]

# Prefix Sum 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

print(prefix_sum)

# index 3~4까지의 구간합은?
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left-1])
