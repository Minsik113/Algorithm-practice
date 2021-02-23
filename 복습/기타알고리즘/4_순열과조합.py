import itertools

data = [1,2,3,4,5]

# 순열
print('순열')
for x in itertools.permutations(data,2):
    print(list(x), end=' ')
print()
print('조합')
for x in itertools.combinations(data, 2):
    print(list(x),end=' ')