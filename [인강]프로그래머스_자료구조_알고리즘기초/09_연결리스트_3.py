'''
중간에 무엇을 빼내거나 적용할 때는 연결리스트가 적당.

장점
삽입과 삭제가 유연하다

insertAfter(prev, newNode) - 어떤 노드의 뒤에 삽입 => 맨 앞 삽입은 어떻게?
popAfter(prev)             - 어떠 노드으 뒤를 pop  => 맨 앞 pop은 어떻게?
-> 맨 앞에 dummy node를 추가함

# dummy node가 head에 추가된 링크드 리스트로 구현해보기 ()
1.길이 얻어내기
2.리스트 순회
3.특정 원소 참조(k번째)
4.원소 삽입
5.원소 삭제
6.두 리스트 합치기
'''

class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None) # 1. 더비 노드 생성
        self.tail = None
        self.head.next = self.tail
    
    def traverse(self): # 리스트순회
        result = [] 
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result
    
    def getAt(self, pos): # pos번째 원소 얻어내기
        if pos < 0 or pos > self.nodeCount:
            return None
        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr