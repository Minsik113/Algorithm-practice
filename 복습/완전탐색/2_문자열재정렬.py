'''
문자열 오름차순정렬
숫자있으면 더해라. 10^4 니까 nlogn = 200만
-> sort()하고 앞에서부터 찾아도 ㄱㅊ음
# ord('0')~ord('9') = 48~57
# ord('a')~ord('z') = 97~122
# ord('A')~ord('Z') = 65~90
'''
##########################################
##########################################
# isalpha()이용하기
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()
if value != 0:
    result.append(value)
print(''.join(result))
exit()
##########################################
##########################################
# ord()이용
strings = list(input())
num_s = []
str_s = []
total = 0
for s in strings:
    if 49 <= int(ord(s)) and int(ord(s)) <= 57: # 숫자면
        # num_s.append(s)
        total += int(ord(s))-48
    else:
        str_s.append(s)

str_s.sort()
if total != 0: # 0일 때도 고려해준다.
    str_s.append(total)
print(''.join(map(str,str_s)))