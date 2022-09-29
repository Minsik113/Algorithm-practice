'''
날짜: 2022.09.29
시간복잡도:

문제: https://www.acmicpc.net/problem/1546
풀이방식:
'''
n = int(input())
scores = list(map(int, input().split()))\

print(sum(scores) / max(scores) * 100 / n)

# [책]Doit_알고리즘_코딩테스트
import random
findNumber = random.randrange(1,101)
for i in range(1, 101):
    if i == findNumber:
        print(i)
        break