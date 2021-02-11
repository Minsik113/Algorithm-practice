'''
# 1/27
# 문제 난이도: Silver 1
# 문제 유형:BFS
# 추천 풀이 시간: 30분
'''
'''
특정 위치까지 이동하는 최단 시간을 계산해야 하는 문제
이동시간이 모두 1초로 동일하다. 간단히 BFS이용해서 해결가능
'''
from collections import deque

n, k = map(int, input().split())
MAX = 100001
array = [0] * MAX

def bfs():
    q = deque([n])
    
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            return array[now_pos]
        for next_pos in (now_pos-1, now_pos+1, now_pos*2):
            if 0 <= next_pos < MAX and not array[next_pos]:
                array[next_pos] = array[now_pos] + 1
                q.append(next_pos)

print(bfs())