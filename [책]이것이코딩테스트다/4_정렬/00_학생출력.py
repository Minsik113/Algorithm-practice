'''
A의 리스트합이 최대가 되게하자
A의 min과 B의 max값을 k번 바꾼다.
N = 10^5  O(nlogn) => 몇백만임. 2번정렬해서 k번바꾸면 2천번안에 됨.

'''
##########################################
##########################################
# 
n, k = map(int, input().split())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

aa.sort() # 제일 작은수 맨앞
bb.sort(reverse=True) # 제일 큰수 맨앞
for i in range(k):
    if aa[i] < bb[i]: 
        aa[i], bb[i] = bb[i], aa[i]
    else:
        break
print(sum(aa))
    

##########################################
##########################################
# 나
# n, k = map(int, input().split())
# aa = list(map(int, input().split()))
# bb = list(map(int, input().split()))

# aa.sort() # 제일 작은수 맨앞
# bb.sort(reverse=True) # 제일 큰수 맨앞
# count = 0
# for i in range(n):
#     # bb의 큰수 < aa의 작은수 -> 끝냄. 바꿀필요 없음
#     if aa[i] > bb[i]: 
#         break
#     else:
#         if count == k: # 바꿀수있는 횟수 없으면 나옴
#             break
#         else: # 바꿀 수 있으면
#             count += 1
# value = sum(bb[:count]) # 0~2 3개바꿈
# value += sum(aa[count:])# 3~n 
# print(value)            
    