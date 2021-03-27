##########################################
##########################################
# 3/27
'''
계차수열로 정렬한 후 
k값을 출력.

'''
n = int(input())
k = int(input())

count = [0] * (n*n +1) # 1~(n*n)이니까
# O(200만)
data = [i*j for i in range(1, n+1) for j in range(1, n+1)]
#O(200만)
for i in range(len(data)):
    count[data[i]] += 1

# count각각에 들어간 애들을 뺴면서 비교한다
print(k,count,len(data))
num = 1
while num <=len(data):
    k -= count[num]
    if k <= 0:
        print(num)
        break
    else:
        num += 1

# ##########################################
# ##########################################
# # 3/27 - heapq는 메모리초과
# '''
# --- heapq - 메모리초과
# n = 10만
# 그냥 minheap에 다 넣는다. O(n^2)
# k번쨰 출력한다
# '''
# import heapq

# n = int(input())
# k = int(input())
# data = []

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         heapq.heappush(data, i*j)

# for i in range(k):
#     if i == k-1:
#         print(heapq.heappop(data))
#         break
#     heapq.heappop(data)