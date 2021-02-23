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

