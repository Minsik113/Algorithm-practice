# 리스트 순회

class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCnt = 0
        self.head = None
        self.tail = None
    
    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCnt:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def getNodeCnt(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node1.next = node2
node2.next = node3
print(node1.data)
print(node1.next)
print(node1.next.data)
print(node2.data)
print(node2.next.data)
print(getNodeCnt)