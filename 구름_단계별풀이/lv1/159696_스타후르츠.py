'''
날짜: 2022.11.21
시간복잡도:

문제:
스타후르츠 심기. 여름에만 자란다. 여름은 N일 동안 지속.
씨앗은 자라는데 T일이 걸림. i일에 심으면 i+T일에 수확가능. 수확한 날 심기도 가능
판매-스타후르츠 1개당 P원. 

풀이:
23:38 ~ 23:52 (14M)

무조건 심을수록이득.

7 3 2 750
2칸에 심기. 3일동안 자라니까
0+3일 = 3일에 2개 수확가능
3+3일 = 6일에 2개 수확가능
총4개
750*4 = 3000

10 2 40 500
40칸에 심기. 2일동안자라니까
2일 = 40개 수확가능
2일에 심어서 2+2일에 40개수확가능
4+2 40
6+2 40
8+2 40
총200개 수확.

1. c개에 모두 심을거다.
1-1.단, now + T <= n 이어야한다.
2. 1번반복
3. 총개수 * p = 가격
'''
n,t,c,p = list(map(int,input().split())) # 여름의 일 수, T, 칸 수, 개당가격

result = 0
cnt = 1
while True:
	temp = cnt * t # 후르츠 자라는 시간 T일
	if temp < n: # 수확이 가능하니까 수확한다. # 여름끝나기전까지해야하네.
		cnt += 1 # 카운트 증가
		result += c # c개만큼 수확
	else:
		break
	# print(temp, cnt, result)
print(result*p)
