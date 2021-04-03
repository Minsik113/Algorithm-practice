import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
x = int(input())

pos = 1
for i in range(0, len(array)-1):
    if array[i]