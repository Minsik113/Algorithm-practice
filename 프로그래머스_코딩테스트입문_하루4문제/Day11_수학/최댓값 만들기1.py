'''
날짜: 2022.12.08
시간복잡도: O(N)

문제:
풀이:
제일큰 수 2개 구하면됨.
최대힙으로 빼면 넣는거만 생각하면됨 O(N+2) # N개 넣고 2개 뽑고

'''
import heapq
def solution(numbers):
    answer = 0
    h = []
    for i in numbers:
        heapq.heappush(h,-i)
    a=heapq.heappop(h)
    b=heapq.heappop(h)
    print(h)
    print(-a,-b)
    
    return -a*-b