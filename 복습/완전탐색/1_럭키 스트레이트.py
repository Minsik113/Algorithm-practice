##########################################
##########################################
# 배열을 1번만봄
strings = list(map(int, input()))
length = len(strings)//2
value = 0

for i in range(length):
    value += strings[i]
for i in range(length,len(strings)):
    value -= strings[i]
if value == 0:
    print("LUCKY")
else:
    print('READY')
exit()
##########################################
##########################################
# 위에꺼보다 배열을 앞부분 더본다.
strings = list(map(int, input()))
length = len(strings)//2
left_strings = sum(strings[:length])
right_strings = sum(strings[length:])
if left_strings == right_strings:
    print("LUCKY")
else:
    print('READY')
