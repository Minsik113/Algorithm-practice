from itertools import combinations

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 2. 좀 더 간략하게
        def dfs(depth, path):
            if len(path) == len(digits):
                result.append(path)
                return
            # 입력값 자릿수 단위 반복
            for i in range(depth, len(digits)):
                # 숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)
        
        # 예외처리
        if not digits:
            return []
        
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        dfs(0, "")
        return result
        
        # 1. 4/14 - 내풀이
#         chart = {
#             '2': ['a', 'b', 'c']
#             , '3': ['d', 'e', 'f']
#             , '4': ['g', 'h', 'i']
#             , '5': ['j', 'k', 'l']
#             , '6': ['m', 'n', 'o']
#             , '7': ['p', 'q', 'r', 's']
#             , '8': ['t', 'u', 'v']
#             , '9': ['w', 'x', 'y', 'z']
#         }
#         result = []
#         s = [''] * (len(digits))

#         # digits의 depth번째 위치에 있는걸 s 에 넣어라
#         def backtracking(depth, s, chart, digits):
#             if depth == len(digits):
#                 result.append("".join(map(str, s)))
#                 return
#             for char in chart[digits[depth]]:
#                 s[depth] = char # 값 추가
#                 backtracking(depth+1, s, chart, digits) # 다음위치에 뭐넣을지 봄
#                 s[depth] = '' # 값 초기화
#             return
        
#         backtracking(0, s, chart, digits)
                
#         if digits == "":
#             return []
#         return result