n = int(input())

start_index = 1
end_index = 1
total = 1
cnt = 1

while end_index != n:
    print(total, n)
    if total == n:
        cnt += 1
        end_index += 1
        total += end_index
    elif total > n:
        total -= start_index
        start_index += 1
    else:
        end_index += 1
        total += end_index
print(cnt)
        