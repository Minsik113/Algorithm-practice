'''
날짜: 2022.12.25
시간복잡도:

문제:
줄세우고 몇번째로 큰지 찾아라

풀이:
20:59~21:05(6분)
방법1.
heapq
방법2.더 빠름
모든 수 다 보면서 height보다 큰 애들 카운트하기
'''
def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer

import heapq
def solution(array, height):
    answer = 0
    h = []
    for i in array:
        heapq.heappush(h,-i)
    heapq.heappush(h, -height)
    while True:
        a = -heapq.heappop(h)
        if a == height:
            break
        answer += 1
            
    return answer