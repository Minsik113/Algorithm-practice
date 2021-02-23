data = [1,2,3,4,1,2,3,4,1,2,1]
n = len(data)
m = 5

count = 0
interval_sum = 0
end = 0

for start in range(n):
    # end를 가능한 만큼 이동시킨다.
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1

    if interval_sum == m:
        count += 1

    interval_sum -= data[start]
    print(data[start],data[end],'z',interval_sum)

