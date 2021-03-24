from collections import deque

array = deque([1,2,3,4,5])
array.rotate(1)
print(array)
array = deque([1,2,3,4,5])
array.rotate(-1)
print(array)