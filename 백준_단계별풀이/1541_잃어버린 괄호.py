'''
55+50-50+40-50
55+50-(50+40)-50
'-' 만나면 -만날때까지 숫자 더한다

'''
s = input()

k = ""
nums = []
oper = []
for i in s:
    if i.isalnum():
        k+=i
    else:
        nums.append(k)
        k = ""
        oper.append(i)
nums.append(k)
# print(nums)
# print(oper)
result = nums[0]

print(result)