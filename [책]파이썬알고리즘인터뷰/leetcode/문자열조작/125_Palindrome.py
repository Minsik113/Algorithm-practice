##########################################
##########################################
# 4/2 - 슬라이싱() 이용
import re # leetcode에는 내장되어있음.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # regular expression filtering
        s = re.sub('[^a-z0-9]', '',s) # '^'는 []안의 문자를 제외한 모든문자를 ''로 변환한다. = 제거
        return s == s[::-1] # 뒤집었을때 같은가

##########################################
##########################################
# 4/2 - deque()이용
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         strs: Deque = collections.deque()
            
#         # only alnum, then convert lower()
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
#         while len(strs) > 1:
#             if strs.popleft() != strs.pop():
#                 return False
#         return True
        
##########################################
##########################################
# 4/2 - pop을 이용해보자
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # only alnum
#         strs = []
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
        
#         # is palindrome ? 
#         while len(strs) > 1:
#             if strs.pop(0) != strs.pop():
#                 return False
#         return True
##########################################
##########################################
# 4/2 - 첫풀이
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         # only alphanumeric
#         result = []
#         for i in range(len(s)):
#             if s[i].isalnum():
#                 result.append(s[i].lower())
#         print(result)
        
#         # s[:half] == s[half:].reverse()
#         length = len(result)
#         for i in range(length // 2):
#             if result[i] != result[length-i-1]:
#                 return False
#         return True
