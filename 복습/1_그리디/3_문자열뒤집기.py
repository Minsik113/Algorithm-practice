array = list(map(int, input()))
check = [0] * 2  # 연속된 0의개수 or 연속된 1의개수

prev = array[0]
check[prev] += 1

for i in range(1, len(array)):
    target = array[i]

    if prev != check: # 바뀐거잖아 -> 추가해줌
        check[target] += 1
    # 안바뀌면 넘어감.
print(min(check))