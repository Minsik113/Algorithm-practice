from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # 3. 2번을 간략히 -> 2회독때 다시 보자
        answer = []
        s = []
        
        def backtracking(array):
            if len(array) == 0:
                answer.append(s[:])
            
            for i in array:
                temp = array[:]
                temp.remove(i) # i 원소 제거
                
                s.append(i)
                backtracking(temp)
                s.pop()
            
                
        backtracking(nums)
        return answer
    
        # 2. 직접 백트래킹 구현
        # result = []
        # path = [0] * (len(nums))
        
        # # 이전에중복된게 있는지 체크한다
        # def check(depth, path):
        #     for i in range(depth):
        #         if path[i] == path[depth]:
        #             return False
        #     return True
        
        # def backtracking(depth, path):
        #     if depth == len(nums):
        #         # result.append(path) 이러면 오류난다 ★★★★★
        #         result.append(path[:])
        #         return
        #     for i in range(len(nums)):
        #         path[depth] = nums[i]
        #         if check(depth, path):
        #             backtracking(depth+1, path)        
            
        # backtracking(0, path)
        # return result
        
        # 1. itertools.permutaions()라이브러리 사용
        # return list(map(list, itertools.permutations(nums)))

#        answer = []
#         for i in list(permutations(nums, len(nums))):
#             answer.append(list(i))
#         return answer
    