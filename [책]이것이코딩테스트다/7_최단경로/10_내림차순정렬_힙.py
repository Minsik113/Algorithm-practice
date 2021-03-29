import heapq

array = [2,3,4,1,6,7,0,10,123,15,62,23]

def heapsort(array):
    h = []
    result = []
    for i in array:
        heapq.heappush(h, -i)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort(array)
print(result)