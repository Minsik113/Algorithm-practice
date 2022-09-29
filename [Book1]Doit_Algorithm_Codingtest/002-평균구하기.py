'''
날짜: 2022.09.29
시간복잡도: O(N)

문제: https://www.acmicpc.net/problem/1546
풀이방식:
'''
n = int(input())
scores = list(map(int, input().split()))\

print(sum(scores) / max(scores) * 100 / n)