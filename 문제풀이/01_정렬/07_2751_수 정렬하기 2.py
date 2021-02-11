# 1/18
# 문제 난이도: Silver 5
# 문제 유형: 정렬
# 추천 풀이 시간: 20분
##### 퀵 정렬, 병합 정렬, 힙 정렬, 기본정렬 ####

# 100만개를 2초안에 풀 효율적인 알고리즘을 세워야한다.
# O(NlogN)의 정렬 알고리즘을 해야함. 
# 1초에 2천만번 계산정도함. 2^10 = 1,000
# 병합정렬, 퀵정렬, 힙정렬. or 파이썬의 기본정렬 알고리즘. 퀵정렬은O(n^2)
# 메모리가 허용된다면, pypy3를 선택하여 코드 제출.

# 병합정렬 O(NlogN) = N의길이 * logN 높이
# divide & conquer
# 절반씩 합치면서 정렬하면, 전체 리스트가 정렬된다.

#######################  ########################  
# 정렬 O(NlogN)임
# 1,000,000 = 10^6 = 대략 2^20
# 시간복잡도에 넣어보자
# 1,000,000 x 20 = 2000만.
# 파이썬 1초에 2천만정도 계산가능. 2초니까 O(NlogN)가능.
# 메모리: 73608kb, 시간: 1572ms
import sys

n = int(sys.stdin.readline().sp)
data = []

for _ in range(n):
    x = int(sys.stdin.readline().split(' '))
    data.append(x)

data.sort()

for i in data:
    print(i)

#######################  ########################  
# 동빈나 - 병합정렬 또는 sort()
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    # 한쪽이 다 찼을경우 나머지를 쭉 이어붙인다.
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    
    return array

import sys

x = int(sys.stdin.readline())
array = []
for _ in range(x):
    array.append(int(sys.stdin.readline()))

array = merge_sort(array)
for i in array:
    print(i)
    
