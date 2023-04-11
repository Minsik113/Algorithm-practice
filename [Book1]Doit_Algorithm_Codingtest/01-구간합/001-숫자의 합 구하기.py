'''
날짜: 2023.04.11
시간복잡도: O(N)

문제: https://www.acmicpc.net/problem/11720
풀이방식:브루트포스
'''
n = int(input())
arr = input()
print(type(arr))
answer = 0
for i in range(n):
    answer += int(arr[i])
print(answer)


'''
날짜: 2022.09.29
시간복잡도: O(N)

문제: https://www.acmicpc.net/problem/11720
풀이방식: 브루트포스
'''
n = int(input())
number = input()
res = 0

for i in range(len(number)):
    res += int(number[i])
print(res)
