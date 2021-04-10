##########################################
##########################################
# 4/10 - 더 깔끔한 풀이
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        for char in s:
            if char not in table: # ( [ {
                stack.append(char)
            # 닫는거 나왔을 때
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0

##########################################
##########################################
# 4/10 - 첫 풀이
# class Solution:
#     def isValid(self, ss: str) -> bool:
#         s = []
#         for temp in ss:
#             print(temp)
#             if temp == ')':
#                 if s and s[-1] == '(':
#                     s.pop()
#                 else:
#                     return False
#             elif temp == ']':
#                 if s and s[-1] == '[':
#                     s.pop()
#                 else:
#                     return False
#             elif temp == '}':
#                 if s and s[-1] == '{':
#                     s.pop()
#                 else:
#                     return False
#             else:
#                 s.append(temp)
#         if not s:
#             return True
#         else:
#             return False
            