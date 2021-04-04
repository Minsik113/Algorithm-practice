class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 3. 2번을 파이썬스럽게 풀자
        return sum(sorted(nums)[::2])
        
        # 2. 짝수번쨰만 본다.
#         nums.sort()
#         result = 0
#         for i, n in enumerate(nums):
#             if i % 2 == 0:
#                 result += n
#         return result
        
        # 1. 2개를 묶어 min(a,b)로 만들 수 있는 최대합구해라
#         nums.sort()
        
#         pair = []
#         result = 0
#         for num in nums:
#             pair.append(num)
#             if len(pair) == 2:
#                 result += min(pair)
#                 pair = []
#         return result