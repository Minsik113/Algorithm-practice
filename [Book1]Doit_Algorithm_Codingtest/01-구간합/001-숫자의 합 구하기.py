'''
날짜: 2022.09.29
시간복잡도:

문제: https://www.acmicpc.net/problem/11720
풀이방식:
'''
n = int(input())
number = input()
res = 0

for i in range(len(number)):
    res += int(number[i])
print(res)