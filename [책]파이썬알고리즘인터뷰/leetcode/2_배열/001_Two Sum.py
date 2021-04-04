class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 3. dict이용 - O(1) ~ O(N)
        # dict에 저장
        nums_map = dict()
        for i, num in enumerate(nums):
            if (target - num) in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i
        
        # 4. 투포인터 - O(NlogN) - O(NlogN) + O(N)임
#         nums = [(val, idx) for idx, val in enumerate(nums)]
#         nums = sorted(nums, key=lambda x:x[0])
#         result = []
#         left = 0
#         right = len(nums) - 1
#         while left < right:
#             temp = nums[left][0] + nums[right][0]
#             if temp > target:
#                 right -= 1
#             elif temp < target:
#                 left += 1
#             else:
#                 return [nums[left][1], nums[right][1]]
        
        # # 2. in을 이용한 탐색 - O(N^2) brute force보다 빠름
#         for idx, val in enumerate(nums):
#             x = target - val
#             if x in nums[idx + 1:]:
#                 return [nums.index(val), nums[idx+1:].index(x)+(idx+1) ]
        
        # 1. 브루트포스 - O(N^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]