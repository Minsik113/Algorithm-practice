'''
작은 수 부터 그룹 묶고 못묶으면 끝내면 최댓값 출력가능하다
1. 리스트 오름차순
2. 리스트[i]값과 count로 적절히 비교

'''
n = int(input())
array = list(map(int, input().split()))
array.sort()

result = 0
count = 1
for i in range(len(array)):
    if array[i] == count:
        result += 1
        count = 1

    else:
        count += 1
print(result)
