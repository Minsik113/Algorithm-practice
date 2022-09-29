'''
날짜:
시간복잡도:

문제: https://www.acmicpc.net/problem/11659
풀이방식:
'''

# [책]Doit_알고리즘_코딩테스트
import random
findNumber = random.randrange(1,101)
for i in range(1, 101):
    if i == findNumber:
        print(i)
        break