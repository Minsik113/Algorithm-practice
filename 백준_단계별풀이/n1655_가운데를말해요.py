
# ##########################################
# ##########################################
# # 모두 시간초과

# # '''
# # n = 10^5
# # O(nlogn) = 700만

# # 매번정렬이 필요함
# # -> 원하는쪽에 값추가

# # 탐색 O(logN)
# # 삽입 O(1)
# # 출력 O(1)
# # '''
# # from bisect import bisect_left, bisect_right
# # import sys
# # input = sys.stdin.readline

# # def find_position(result, data):
# #     return bisect_left(result, data)

# # n = int(input())
# # result = []
# # answer = []
# # for i in range(1, n+1): # i는 현재 배열의 길이로 하자.
# #     x = int(input())
# #     if not result:
# #         result.append(x)
# #     else:
# #         pos = find_position(result, x)
# #         result.insert(pos, x)

# #     k = result[i//2 - 1] if i % 2 == 0 else result[i//2]
# #     answer.append(k)
# # # print(result)
# # # print(answer)
# # for i in answer:
# #     print(i)
    
    

# # # '''
# # # 지금까지 말한 수 중 중간값을 말한다.

# # # if 개수가 짝수라면) 두 수중 작은수를 출력.
# # # -> 우선순위 큐를 이용해서 계속넣는다.
# # # # 짝수개라면 h[len(h) // 2 - 1]
# # # if len(h) % 2 == 0: 
# # # # 홀수개라면 h[len(h)//2]

# # # '''
# # # '''
# # # 바로바로 정렬어떻게하지? 
# # # -> 1~n길이까지 매번 정렬해주는건 너무 길다.

# # # insert로 위치찾아서 삽입을할까? 그러면
# # # 매번 O(n)이니까

# # # '''
# # # import sys, heapq
# # # input = sys.stdin.readline

# # # n = int(input())
# # # q = []
# # # length = 0
# # # result = []

# # # for i in range(n):
# # #     x = int(input())
# # #     heapq.heappush(q, x)
# # #     length += 1
# # #     if length % 2 == 0:
# # #         # print(h[length//2 - 1])
# # #         result.append(q[length//2 - 1])
# # #     else:
# # #         # print(h[length//2])
# # #         result.append(q[length//2])
# # # print(q)
# # # print(result)