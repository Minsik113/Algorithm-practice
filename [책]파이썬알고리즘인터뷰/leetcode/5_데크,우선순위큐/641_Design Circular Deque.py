##########################################
##########################################
# 4/11 - 연결리스트를 구현해서 풀어볼까 ?
# -> 2회독때 다시보자~


##########################################
##########################################
# 4/11 - 첫풀이 그냥 deque로 풀음
from collections import deque

class MyCircularDeque:

    def __init__(self, k: int):
        self.q = deque()
        self.max_length = k
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.count < self.max_length:
            self.q.appendleft(value)
            self.count += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.count < self.max_length:
            self.q.append(value)
            self.count += 1
            return True
        return False
        

    def deleteFront(self) -> bool:
        if self.q:
            self.q.popleft()
            self.count -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.q:
            self.q.pop()
            self.count -= 1
            return True
        return False
        

    def getFront(self) -> int:
        return self.q[0] if self.q else -1
        

    def getRear(self) -> int:
        return self.q[-1] if self.q else -1
        

    def isEmpty(self) -> bool:
        return True if self.count == 0 else False

    def isFull(self) -> bool:
        return True if self.count == self.max_length else False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()