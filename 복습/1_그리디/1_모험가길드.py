'''
그리디. 
1. 입력받은 array리스트 정렬한다
2. 하나씩 개수 센다.(count)
3. pos가 한칸씩 이동한다.
4. 개수 == array[pos] 라면 result +=1 and count = 0
5. pos가 끝에 도달할 때까지 보면 된다.
=> 최소한의 모험가로 최대팀을 꾸려 모험할 수 있다.
'''

n = int(input())
array = list(map(int, input().split()))
array.sort()

count = 1 # 현재 그룹원 수
result = 0 # 총 그룹 수

for pos in range(len(array)):
    if count == array[pos]:
        result += 1
        count = 1
    else:
        count += 1

print(result)
