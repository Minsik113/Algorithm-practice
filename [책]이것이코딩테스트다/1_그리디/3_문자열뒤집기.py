'''
1. 연속된 0 or 1의 개수를 센다.
2. 작은 수 출력

'''
##########################################
##########################################
# 3/16 이전거를 바꿔줌
# data = list(map(int, input()))
# count = [0] * 2

# pre = data[0] # 처음수
# save = 0
# for i in range(1, len(data)):
#     if pre != data[i]: # 이전값과 다르면 
#         count[pre] += 1 # 이전값의 count증가, 
#         pre = data[i] # 이전값을 현재값으로
# count[pre] += 1 # 마지막에 나온값

# print(min(count))

##########################################
##########################################
# 2/24 현재꺼를 바꿔줌
arr = list(map(int, input()))
# 0, 1 이 들어갈 변수
check = [0] * 2

# 첫번째꺼 등록
check[arr[0]] += 1

# 첫번째랑 다르면 반대쪽 올려준다
for i in range(1, len(arr)):
    if arr[i] != arr[i-1]:
        check[arr[i]] += 1
print(min(check))
print(check)
