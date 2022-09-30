'''
날짜: 2022.09.29
시간복잡도: O(N^2)

문제: https://www.acmicpc.net/problem/11660
풀이방식: 
20:25 ~ 20:59

n범위가 작으니 부분합 표 만들어 두자
D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i-1][j-1]

테스트
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 1. 맵입력
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
# 2. 부분합 맵 입력 
numbers = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1): # D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i-1][j-1]
    for j in range(1, n+1):
        numbers[i][j] = numbers[i-1][j] + numbers[i][j-1] - numbers[i-1][j-1] + arr[i-1][j-1]
# print(numbers)
# print()
# 3. 타겟부위 합
for i in range(m): # D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    x1,y1,x2,y2 = list(map(int, input().split()))
    
    print(numbers[x2][y2] - numbers[x1-1][y2] - numbers[x2][y1-1] + numbers[x1-1][y1-1])


