n, m = map(int, input().split())
array = list(map(int, input().split()))

count = [0] * 11 # m은 1~10
for x in array:
    count[x] += 1

# 개수 다 셌으면 해당무게로 조합할수있는 개수를 세면됨
result = 0
for i in range(1, m+1):
    n -= count[i] # 현재있는애들개수
    result += count[i] * n

print(result)


# # 매번 체크해야하므로 느림 O(N^2)
# n, m = map(int, input().split())
# array = list(map(int, input().split()))

# # 전체개수 - 같은애 개수
# result = 0
# for i in range(n):
#     for j in range(i,n):
#         if array[i] != array[j]:
#             result += 1
# print(result)