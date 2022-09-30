'''
날짜: 2022.10.01
시간복잡도:

문제: https://www.acmicpc.net/problem/1253
풀이방식:
01:07 ~ 

n = 2000
1.정렬
2.앞 뒤에 두고 시작

'''

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0

for k in range(n):
    find = arr[k]
    i = 0
    j = n-1
    while i < j:
        if arr[i] + arr[j] == find:
            if i != k and j != k:
                result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif arr[i] + arr[j] < find:
            i += 1
        else:
            j -= 1
