'''
추상적 자료구조 (Abstract Data Structure)
삽입, 삭제, 순회,..
정렬, 탐색

Node
 - Data
 - Link(next)
노드내의 Data는 다른 구조로 이루어질 수 있다.
ex) 문자열, 레코드, 또 다른 연결 리스트 등 

#배열 - O(1)
저장공간 - 연속한 위치
특정 원소 지칭 - 매우 간편

#연결리스트 - O(n)
저장공간 - 임의의 위치
특정 원소 지칭 - 선형탐색과 유사

1.특정 원소 참조(k번째)
2.리스트순회
3.길이 얻어내기
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
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos <= 0 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

node1 = Node(1)
node2 = Node(3)
node1.next = node2
print(node1.data)
print(node1.next)
print(node1.next.data)
print(node2.data)
print(node2.data)