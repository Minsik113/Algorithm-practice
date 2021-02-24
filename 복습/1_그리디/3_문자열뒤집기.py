'''
1. 연속된 0 or 1의 개수를 센다.
2. 작은 수 출력

'''
##########################################
##########################################
# 다시품
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
##########################################
##########################################
# 
# array = list(map(int, input()))
# check = [0] * 2  # 연속된 0의개수 or 연속된 1의개수

# prev = array[0]
# check[prev] += 1

# for i in range(1, len(array)):
#     target = array[i]

#     if prev != check: # 바뀐거잖아 -> 추가해줌
#         check[target] += 1
#     # 안바뀌면 넘어감.
# print(min(check))