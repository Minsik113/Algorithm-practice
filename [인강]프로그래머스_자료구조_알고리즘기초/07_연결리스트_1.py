'''
추상적 자료구조 (Abstract Data Structure)
삽입, 삭제, 순회,..
정렬, 탐색

Node
 - Data
 - Link(next)
노드내의 Data는 다른 구조로 이루어질 수 있다.
ex) 문자열, 레코드, 또 다른 연결 리스트 등 

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



