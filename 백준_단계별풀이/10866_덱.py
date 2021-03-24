##########################################
##########################################
# 3/24 - 더 깔끔한 풀이? (다른사람)
'''
dict자료형을 이용해 switch-case를 구현
'''
import sys
input = sys.stdin.readline

def push_front(deq, x):
    tmp = [x]
    tmp.extend(deq) # 뒤에 이어붙인다.
    deq = tmp
    return deq

def push_back(deq, x):
    deq.append(x)
    return deq

def pop_front(deq):
    if deq:
        print(deq.pop(0))
    else:
        print(-1)
def pop_back(deq):
    if deq:
        print(deq.pop())
    else:
        print(-1)

def size(deq):
    print(len(deq))
def empty(deq):
    if not deq:
        print(1)
    else:
        print(0)
def front(deq):
    if deq:
        print(deq[0])
    else:
        print(-1)
def back(deq):
    if deq:
        print(deq[-1])
    else:
        print(-1)

statements_dict = {
    'push_front' : push_front
    , 'push_back' : push_back
    , 'pop_front' : pop_front
    , 'pop_back' : pop_back
    , 'size' : size
    , 'empty' : empty
    , 'front' : front
    , 'back' : back
}
n = int(input())
deq = []

for _ in range(n):
    statement = input().rsplit()
    if len(statement) == 1:
        cmd = statement[0]
        statements_dict[cmd](deq)
    else:
        cmd, x = statement
        deq = statements_dict[cmd](deq, x)

##########################################
##########################################
# 3/24 - 단순 풀이
# import sys
# input = sys.stdin.readline

# array = []
# for _ in range(int(input())):
#     string = input().rstrip()

#     if 'push' in string:
#         s = string.split()
#         # push_back
#         if 'back' in string: 
#             array.append(s[1])
#         # push_front
#         else: 
#             array.insert(0, s[1])
#     elif 'pop' in string:
#         if len(array) == 0:
#             print(-1)
#         # pop_front
#         elif 'front' in string:
#             print(array.pop(0))
#         # pop_back
#         else:
#             print(array.pop())
#     elif 'size' in string:
#         print(len(array))
#     elif 'empty' in string:
#         if len(array) != 0: # 값이 존재하면 0
#             print(0)
#         else:
#             print(1)
#     elif 'front' in string:
#         if len(array) == 0:
#             print(-1)
#         else:
#             print(array[0])
#     elif 'back' in string:
#         if len(array) == 0:
#             print(-1)
#         else:
#             print(array[-1])

