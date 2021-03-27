'''
배열에 자연수 x를 넣는다.
배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
'''
import heapq, sys
input = sys.stdin.readline

n = int(input())
h = []

for i in range(n):
    x = int(input())
    # 가장 작은값 출력 및 제거
    if x == 0:
        try:
            print(-heapq.heappop(h))
        except:
            print(0)
    # 리스트에 값 추가
    else:
        heapq.heappush(h, -x)
