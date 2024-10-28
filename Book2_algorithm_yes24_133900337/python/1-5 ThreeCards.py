'''
날짜: 2024.10.28
시간복잡도: O(N^2)
시간: 21:00 ~ 21:38
문제: A05 Three Cards
풀이방식: 
  1. 1~n까지의 카드 3장의 합이 K가 되는 경우의 수는?
  2. 경우의 수 다 세자.
    if 셋 다 다를 경우, 3P2 = 6개
    if 하나만 다를 경우, 3P1 = 3개
    if 셋 다 같은 경우, 3P0 = 1개
  3. 숫자 조합을 집합에 저장해서 존재하는지 찾자.

'''

n, k = map(int,input().split())
cnt = 0
for x in range(1, n+1):
  for y in range(1,n+1):
    z = k-x-y
    if z >= 1 and z <= n:
      cnt += 1
print(cnt)