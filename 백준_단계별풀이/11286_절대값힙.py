'''
1/ 배열에 정수 x (x ≠ 0)를 넣는다.
2/ 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 
절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 
그 값을 배열에서 제거한다.
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
            print(heapq.heappop(h)[1])
        except:
            print(0)
    # 리스트에 값 추가
    else:
        heapq.heappush(h, (abs(x),x)) # (절대값, 원래값)
