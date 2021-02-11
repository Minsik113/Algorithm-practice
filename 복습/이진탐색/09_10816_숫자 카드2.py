# 1/20
# from collections import Counter
# counter로 하면 쉽게 풀리나봄

def Bsearchtree(array, target):
    start = 0
    end = x - 1

    while (start <= end):
        mid = (start + end) // 2

        if array[mid] == target:
            return data[target]

        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return 0

x = int(input())
x_list = list(map(int, input().split(' ')))
y = int(input())
y_list = list(map(int, input().split(' ')))

x_list.sort()

data = dict()
for i in x_list:
    if i not in data:
        data[i] = 1
    else:
        data[i] += 1

for i in y_list:
    print(Bsearchtree(x_list, i), end=" ")
