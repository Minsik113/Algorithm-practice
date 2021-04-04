'''
s[::-1] 도 결과는 나오지만 공간복잡도를 O(1)로 제한하여서 제약이 생긴다.
'''
##########################################
##########################################
# 4/2 - 단순풀이
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
    
##########################################
##########################################
# 4/2 - 투포인터사용 ( C 풀이느낌 )
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         left, right = 0, len(s) - 1
#         while left < right:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1