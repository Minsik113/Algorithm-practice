####################
# 날짜: 2023.10.29
# 시간복잡도:
# 해결시간: 9뷴 (13:00~13:09)
# 포인트:
# 
#
#
####################
import math
a = [int(input()) for _ in range(5)]

flag = False
start = 1
for i in a:
    start = start*i
    # print(start)
    if math.sqrt(start) == int(math.sqrt(start)):
        flag = True
        break
if flag:
    print("found")
else:
    print("not found")