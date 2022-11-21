'''
날짜: 2022.11.21
시간복잡도: O(N)

문제:
문자열을 앞에서부터 문자 비교.
같으면 합치고 다르면 그냥 둠. 총 길이

풀이:
23:30 ~ 23:35

1. prev=s[0], cnt = 1
2. prev랑 현재랑 비교
2-1. 같으면 pass
2-2. 다르면 prev = s[now], cnt + 1

'''
n = int(input())
s = list(map(str,input()))

prev = s.pop()
cnt = 1
while s:
	now = s.pop()
	if prev == now: # 2-1
		pass
	else: # 2-2
		prev = now
		cnt += 1
print(cnt)