'''
nxm 
0: 이동
1: 이동x

0,0 -> n-1,m-1
최단경로.
시작과 끝의 개수를 포함한다.

그냥갈때 or 벽하나부숴서갈떄 
- 짧은게 답.

'''
from collections import deque

n, m = map(int, input().split())
