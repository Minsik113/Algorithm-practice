'''
1. 2개 조합을 모두 구한다
2. 모든 조합개수 - (무게 같은거).
-> 원하는 답 나옴
'''

##########################################
##########################################
# 단순코딩 - 비효율적 
from itertools import combinations
import time 
n, m = map(int, input().split())
array = list(map(int, input().split()))
start_time = time.time()
pair = list(combinations(array,2))
count = len(pair)
for i in range(len(pair)):
    a, b = pair[i][0], pair[i][1]
    if a == b:
        count -= 1
print(count)
end_time = time.time()
print(end_time-start_time)
