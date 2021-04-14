##########################################
##########################################
# 4/14 - 방법 2개
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # 2. pythonic하게
        # print(collections.Counter(nums).most_common(k)) # 빈번도가 큰것순으로 출력
        # print(list(zip(*collections.Counter(nums).most_common(k)))[0])
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
        
        # 1. Counter + heapq
#         a = collections.Counter(nums)
#         h = []
        
#         # max-heap (개수, 값)
#         for i in a:
#             # print(i,a[i]) # (key, value)
#             heapq.heappush(h, (-a[i], i)) # 즉, (개수, key)
        
#         result = []
#         for _ in range(k):
#             result.append(heapq.heappop(h)[1]) # key
#         # print(result)
#         return result
#         # print(sorted(result))
#         # return sorted(result)