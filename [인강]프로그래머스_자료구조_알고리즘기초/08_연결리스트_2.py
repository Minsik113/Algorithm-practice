'''
1.특정 원소 참조(k번째)
2.리스트순회
3.길이 얻어내기  
4.원소 삽입  - 오늘부터 여기
5.원소 삭제
6.두 리스트 합치기

원소의 삽입 
맨앞 - O(1)
중간 - O(n)
맨끝 - O(1)

원소의 삭제
맨앞 - O(1)
중간 - O(n)
맨끝 - O(n)
''' '''
prev  newNode  pos

1. newNode.next = prev.next
2. prev.next = newNode
3. nodeCount += 1

1. 위치찾기
 prev = self.getAt(pos-1)
 newNode.next = prev.next
 prev.next = newNode
 nodeCount += 1

주의사항
-삽입하려는 위치가 리스트 맨 앞일 때
 prev 없음
 head 조정 필요
-삽입하려는 위치가 맨 끝일 때
 Tail 조정 필요
-빈 리스트에 삽입할 때?
 이 두 조건에 의해 처리됨
-삽입하려는 위치가 리스트 맨 끝일 때,
 pos==nodeCount+1일 때 맨앞부터찾을 필요가없다(getAt()할 필요가없다)
========================
prev curr pos
prev.next = curr.next
nodeCount -= 1

주의사항
-삽입하려는 node가 맨 앞의 것일 때
 prev 없음
 head 조정 필요
-리스트 맨 끝의 node를 삭제할 때
 tail 조정 필요
-유일한 노드를 삭제할 때
 이 두 조건에 의해 처리 되는가????
-삭제하려는 node가 마지막 node 일 떄,
 즉 pos == nodeCount인 경우, prev를 찾을 방법이 없으므로 앞에서부터 찾아야함.


'''


