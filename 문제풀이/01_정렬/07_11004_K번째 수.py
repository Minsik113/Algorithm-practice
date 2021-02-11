# 1/18
# 문제 난이도: Silver 5
# 문제 유형: 정렬
# 추천 풀이 시간: 25분
##### 퀵 정렬, 병합 정렬, 힙 정렬, 기본정렬 ####
# 수도 많아서 계수정렬 안됨.
# O(NlogN)을 보장하는 고급정렬알고리즘을 사용해야한다.
# 100만이 log2^22
# 5,000,000 x 22 => 1억
#

# 메모리 620096kb, 시간 4000ms
import sys

n, idx = map(int, input().split(' '))
#print(n,idx)

data = list(map(int, sys.stdin.readline().split(' ')))

data.sort()
print(data[idx-1])
