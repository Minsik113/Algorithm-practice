from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 3번. 런너풀이 - 다른것들보다 훨씬 빠름. 210p참고
        rev = None
        slow = fast = head
        # print('1',head)
        
        # 역순 연결 리스트 구성
        # Tip. 다중할당 
        while fast and fast.next: # 현재, 다음 존재한다면
            fast = fast.next.next # 다음의 다음을 저장
            rev, rev.next, slow = slow, rev, slow.next
        if fast: # 홀수개라면 한개 남음
            slow = slow.next
        
        # 팰린드롬 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        
        # 정상-> 모두끝까지 이동하여 None이나옴
        return not rev
        
        # 2번. 1번풀이랑 같음
#         q: Deque = collections.deque()
        
#         if not head:
#             return True
        
#         node = head
#         # 리스트변환
#         while node is not None:
#             q.append(node.val)
#             node = node.next
#         while len(q) > 1:
#             if q.popleft() != q.pop():
#                 return False
#         return True
        
        # 1번. 첫풀이
#         q = deque()
#         while head.next != None:
#             q.append(head.val)
#             head = head.next
#         q.append(head.val)
        
#         result = True
#         while len(q) >= 2:
#             if q.pop() != q.popleft():
#                 result = False
#                 break
        
#         return result
        