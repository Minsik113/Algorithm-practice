class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None
        
    # Add new node at the end of the linked list
    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = node

    # node of specific position
    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount: # 없음 or 초과
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr
    
    # insert Elements to a linked list (1<=pos<=nodeCount+1)
    # return value -> bool
    def insertAt(self, pos, newNode): 
        # exception)  
        if pos < 1 or pos > self.nodeCount+1:
            return False
        # 맨앞에 삽입
        if pos == 1:
            newNode.next = self.head # 1
            self.head = newNode # 2
        # 중간에 삽입
        else:
            if pos == self.nodeCount+1:
                prev = self.tail
            else:
                prev = self.getAt(pos-1)
            newNode.next = prev.next
            prev.next = newNode
        # 맨끝에 삽입 
        if pos == self.nodeCount+1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    # insert Elements to a linked list (1<=pos<=nodeCount+1)
    # return value -> data
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        prev = self.getAt(pos-1)
        delNode = prev.next # 삭제할 노드
        
        # 맨앞꺼를 뺌
        if pos == 1:
            delNode = self.head
            self.head = delNode.next
        # 중간꺼+맨뒤를 뺌
        else:
            prev = self.getAt(pos-1) # 삭제 앞 노드 
            delNode = prev.next # 삭제할 노드
            prev.next = curr.next 
        if pos == self.nodeCount+1:
            self.tail = prev
        self.nodeCount -= 1
        return delNode.data

    # Merge two Linked lists
    def concat(self, L):
        self.tail.next = L.head # 붙이기
        if L.tail:
            self.tail = L.tail # tail은 L의 tail
        self.nodeCount += L.nodeCount

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result
    

if __name__ == "__main__":
    sl = LinkedList()
    sl.append(Node(1))
    sl.append(Node(2))
    sl.append(Node(3))
    sl.append(Node(5))
    print(sl.traverse())



