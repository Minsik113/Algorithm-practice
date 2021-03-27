'''
k개의 랜선으로 n개의 랜선을 만들고싶다.
(n개 이상으로 만드는것도 ㄱㅊ음)
이걸 만족할때 최대로 랜선의 길이는?
k = 10^4 = 1만
n = 10^6 = 100만

==1. 이진탐색
1. 중간값으로 선들을 잘라본다.
2. 자르는도중 n 개넘으면 현재자르던길이를 저장하고 mid를 늘려서 다시봄
3. 잘랐는데 n 안넘으면 길이 줄여서 다시 잘라본다
3. 2,3 반복
4. 최대길이 출력

정렬안해도되고 1과 max값으로 하자.
한번 비교하는데에 O(N)
비교할 길이가 최대 logN이라하면
O(NlogN)??
'''
##########################################
##########################################
# 3/27 - 좀더 빠르게 [] 써서구하기
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
data = [int(input()) for _ in range(k)]

start = 1
end = max(data)
max_value = 0 # 0보단 클테니까
while start <= end:
    mid = (start + end) // 2
    count = sum([ i//mid for i in data])
    if count >= n :
        start = mid + 1
        max_value = mid
    else:
        end = mid - 1

print(max_value)


##########################################
##########################################
# 3/27 - 평소풀이
# import sys
# input = sys.stdin.readline

# k, n = map(int, input().split())
# data = [int(input()) for _ in range(k)]

# start = 1
# end = max(data)
# max_value = 0 # 0보단 클테니까
# while start <= end:
#     mid = (start + end) // 2 
#     # mid로 data의 원소들을 자를것이다
#     count = 0
#     for i in range(k):
#         count += data[i] // mid
#         # 만약 개수 넘어가면 크기 늘려서 보자
#         if count >= n: 
#             max_value = mid
#             start = mid + 1
#     # 전부다 봤는데 개수가 조건을 안넘으면 줄여서 다시봄
#     if count < n:
#         end = mid - 1
# print(max_value)

