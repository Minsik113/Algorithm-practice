'''
선택정렬 O(N^2)
특정리스트에서 가장작은 값 찾을때 n 이면 끝남. 
heapq로 N길이 정렬하면 nlog.  O(logN)만에 제일작은수 뽑아냄
-> heappush()가 O(logN)이니까 N개면 NlogN임.
-> 제일작은값찾을땐 O(N걸리는) 선택정렬이 제일 빠르긴하겠네.

삽입정렬 O(N^2)
처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입한다.

'''
## 선택정렬 ## O(N^2)
array = [1,5,2,7,4,10,123,2,20593,0,6,8,9,14]
for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
print(array) # [0, 1, 2, 2, 4, 5, 6, 7, 8, 9, 10, 14, 123, 20593]
        
## 삽입정렬 ## O(N^2)
array = [1,5,2,7,4,10,123,2,20593,0,6,8,9,14]

for i in range(1, len(array)):
    for j in range(i,0,-1): # index i->1 까지 감소
        if array[j] < array[j-1]: # 한칸씩 왼쪽으로이동
            array[j], array[j-1] = array[j-1], array[j]
        else: # 자신보다 작은 값을 만나면 그 위치에서 멈춤
            break
print(array)
