
# # k번째 라는뜻은 앞에 k-1개가 있다는 말이다.
# n = int(input())
# k = int(input())
# start = 1
# end = k
# answer = 0
# while start <= end:
#     mid = (start + end) // 2
#     cnt = 0
#     for i in range(1, n+1):
#         cnt += min(mid//i, n)
#     if cnt >= k:
#         answer = mid
#         end = mid - 1
#     else:
#         start = mid + 1
# print(answer)

# # ##########################################
# # ##########################################
# # # 3/27 - 왜 이것도 메모리초과지
# # '''
# # 계차수열로 정렬한 후 
# # k값을 출력.
# # N=10만
# # O(NlogN) = 10만 x 10 x log100 = 10만 x 70 = 700만

# # 700만 + 700만 정도 메모리부족이 왜 나 ㄹ 까 . ? 
# # '''
# # n = int(input())
# # k = int(input())

# # count = [0] * (n*n +1) # 1~(n*n)이니까
# # # O(700만)
# # for i in range(1, n+1):
# #     for j in range(1, n+1):
# #         count[i*j] += 1
# # # count각각에 들어간 애들을 뺴면서 비교한다
# # print(count)
# # for i in range(1, len(count)):
# #     k -= count[i]
# #     if k <= 0:
# #         print(i)
# #         break

# # # ##########################################
# # # ##########################################
# # # # 3/27 - heapq는 메모리초과
# # # '''
# # # --- heapq - 메모리초과
# # # n = 10만
# # # 그냥 minheap에 다 넣는다. O(n^2)
# # # k번쨰 출력한다
# # # '''
# # # import heapq

# # # n = int(input())
# # # k = int(input())
# # # data = []

# # # for i in range(1, n+1):
# # #     for j in range(1, n+1):
# # #         heapq.heappush(data, i*j)

# # # for i in range(k):
# # #     if i == k-1:
# # #         print(heapq.heappop(data))
# # #         break
# # #     heapq.heappop(data)