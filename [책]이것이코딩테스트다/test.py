import heapq
a = [4,5,6,7,8]
h = []

for idx, i in enumerate(a):
    heapq.heappush(h, [idx, i])
print(h)
while h:
    heapq.heappop(h)
    print(h)