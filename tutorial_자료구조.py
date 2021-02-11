a=['a','d','b','c']
a.append('d')
a.insert(0,'a')
del a[0]
a.remove('a')
len(a)
a.pop()
a. clear()
a.count('a')
a.sort(reverse=True)
a.reverse()
b=[]
a.copy()

# Queue
from collections import deque
queue = deque(['eric','john','michael'])
queue.append('qwe')
queue.popleft()

squares = []
for x in range(10):
    squares.append(x**2)
    
squares
squares1 = list(map(lambda x: x**2,range(10)))
squares2 = [x**2 for x in range(10)]

[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]


matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

list(zip(*matrix))

t = 123, 456, 'qwer'
x,y,z = t     

# import sys
# input() = sys.stdin.readline().rstrip()
import sys 
x = list(sys.stdin.readline().rstrip())
print(x)

a = list(input())
print(a)

# 문자열에서 문자찾기 set()
a = set('abracadabra')
b = set('alacazam')

'a' in a
z = {x for x in 'abracadabra' if x not in 'abc'}
for x in 'abracadabra':
    print(x)

# dictionary
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] =4127
tel
list(tel)
sorted(tel)
'guido' in tel
{x: x**2 for x in (2,4,6)}

knights = {'gallahad':'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k,v)

for i, v in enumerate(knights):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lan', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('what is your {0}? it is {1}'.format(q,a))

(1, 2, 3)              < (1, 2, 4)

name = 'michael'
phone = 1234

f'{name}\'s phone number is {phone}'
