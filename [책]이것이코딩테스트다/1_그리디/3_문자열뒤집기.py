##########################################
##########################################
# 4/22 
s = list(map(int, input()))
count = [0] * 2 # 0, 1의 연속된 개수

prev = s[0]

for i in range(1, len(s)-1):
    if prev == s[i]:
        pass
    else:
        count[prev] += 1
        prev = s[i]
# 끝에 2개가 다르면        
if s[-1] != s[-2]:
    count[0] += 1
    count[1] += 1
else: # 끝에 2개 같으면
    count[s[-1]] += 1

print(min(count))


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
