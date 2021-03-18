'''
숫자는 더하고 알파벳은 오름차순
알파벳 - 숫자 순서
'''

data = input()
alpha = []
total = 0

for i in data:
    if i.isalpha():
        alpha.append(i)
    else:
        total += int(i)
alpha.sort()
if total != 0:
    alpha.append(str(total))
print("".join(map(str,alpha)))

