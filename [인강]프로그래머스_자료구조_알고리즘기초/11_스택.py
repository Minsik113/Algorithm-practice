'''
STACK - First In Last Out

size()      현재 스택에 들어있는 데이터 원소의 수
isEmpty()   현재 스택이 비어있는지를 판단
push(x)     x를 스택에 추가
pop()       맨 위 원소 제거 및 반환
peek()      맨 위 원소
''' 
# 양방향 링크드리스트로 stack구현
# from doublylinkedlist import Node


# 일반적인 stack
class ArrayStack:

    def __init__(self):
        self.data = []
    
    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0
    
    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

'''
수식의 괄호 유효성 검사

1. 왼쪽부터 하나씩 보자
2. 여는괄호 -> push in stack
3. 닫는괄호 -> 스택이 비어있다면) 실패
              스택의 pop과 쌍을 이룬다면) 성공
                          쌍을 이루지 않는다면) 실패
4. 끝까지 검사한 후, 스택이 비어있다면) 성공
'''