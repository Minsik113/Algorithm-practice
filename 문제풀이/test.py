'''
ord('1') = 49
ord('a') = 65
'''
data = input()

num = 0
alpha = []
for x in data:
    if ord(x)-ord('A') < 0: # 숫자라면
        num += int(x)
    else:
        alpha.append(x)
alpha.sort()
print(''.join(map(str,alpha)) + str(num))