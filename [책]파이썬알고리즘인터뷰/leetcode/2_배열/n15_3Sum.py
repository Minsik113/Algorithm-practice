'''
완전탐색 = O(N^3)이다. 이를 줄여야함.
'''
# 4/2 - 실패
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
        
#         nums.sort()
#         result = []
        
#         # O(N^2)
#         for i in range(0, len(nums)-2):
#             if i > 0 and nums[i] == nums[i-1]: # 같은 조합은 중복되기 때문에 빼려고
#                 continue
#             # 2개변수 -> 투포인터 O(N)
#             left = i+1
#             right = len(nums) - 1
#             while left < right:
#                 temp = nums[i] + nums[left] + nums[right]
                
#                 if temp > 0:
#                     right -= 1
#                 elif temp < 0:
#                     left += 1
#                 else:
#                     result.append([nums[i], nums[left], nums[right]])
                    
#                     while left < right and nums[left] == nums[left + 1]:
#                         left += 1
#                     while left < right and nums[right] == nums[right - 1]:
#                         right -= 1
                    
#                     left += 1
#                     right -= 1
#         return result
        