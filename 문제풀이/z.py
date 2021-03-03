from itertools import permutations
numbers = "011"
answer = 0
data = list(map(str, numbers))
length = len(numbers)

save = dict()
for i in numbers:
    if i not in save:
        save[i] = 0
for i in range(2, length+1):
    for j in permutations(data,i):
        print(j)
        # print(list(j))
        if j not in save:
            save[j] = 0
print(save)

for num in save.keys():
    print("".join(num))
for num in save.keys():
    print(type("".join(num)))