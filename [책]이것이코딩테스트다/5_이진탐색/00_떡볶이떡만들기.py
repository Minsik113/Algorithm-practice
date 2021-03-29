'''
1. 떡 길이를 정렬시킴
2. 제일 짧은 떡, 제일 긴 떡
3. 떨어진 떡의 길이합(total)이 m보다 크거나같으면:
result에 max(현재, 지금 자른길이)를 저장하고, 자르는 기준을 길게하여 더 잘라본다
4. 떨어진 떡의 길이합이 m보다 작으면:
길게해서 본다.
'''
n, m = map(int, input().split())
array = list(map(int, input().split()))

# array.sort() # 2천만 시간 => 할 필요없음
# 이진탐색시작
start = 0 # 0 ~ max(떡)의 길이 사이의 값을 찾을것이므로
end = max(array) 
result = 0
while start <= end:
    mid = (start + end) // 2  # 중간 길이로 자름
    total = 0
    for i in array:
        if i > mid:
            total += i - mid
    if total >= m: # 요청한 떡의 길이보다 많이 남았다면 길게해서 더 잘라본다
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)

'''
n떡개수 10^6
->O(nlogn)정렬
m요청한 떡길이 ~ 2x10^9
->O(logM)해야함 = 31 
-> 31 x 10^6 = 3000만번 2초내에 가능.

-> 1. 떡의길이의 중간값(mid)
-> 2. mid로 각 떡을 잘랐을때 남은 길이들의 합이 m보다 작은지본다
-> 3. m이상으로 가장 가깝게 나왔을 떄 mid값이 최대높이다.
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

def binary_search_tree(array, m, start, end): # 
    check = 0
    while start <= end:
        count = 0
        mid = (start + end) // 2
        
        # 이제 다 잘라본다.
        for i in range(len(array)):
            if array[i] > mid:
                count += array[i] - mid
        # 자르고 남은 길이의 합(count)과 m비교
        if count >= m: # 너무 많이 잘렸으면 길이를 길게 해야지
            start = mid + 1
            # check = min(check, count)
            check = mid # 최대한 덜 잘랐을때가 정답. 정렬된 리스트에서 보기때문에 커지면쭉커지고 작아지면 계속작아진다.
        else:
            end = mid - 1
    return check

result = binary_search_tree(array, m, 0, max(array))
print(result)

