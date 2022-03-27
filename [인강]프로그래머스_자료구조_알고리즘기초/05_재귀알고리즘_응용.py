''' 
조합 n! / (m!(n-m)!)
n개의 서로 다른 원소에서 m 개를 택하는 경우의 수
재귀사용할때 잦은 실수 - Trivial case를 고려하지 않은 실수가 빈번하다


'''

'''
하노이의 탑
input: 원판개수, 시작위치, 옮길위치, 임시위치
A의 n개의 원판을 C로 옮기자. 
1. n-1개를 B로 옮긴다.
2. 크기가 n인원판을 C로 옮긴다
3. B에 있는 n-1개의 원판을 C로 옮긴다.
'''
def hanoi(n, from_pos, to_pos, t):
    if n == 1:
        print("시작위치:",from_pos," 도착위치:",to_pos)
        return
    hanoi(n-1, from_pos, t, to_pos)
    print("시작위치:",from_pos," 도착위치:",to_pos)
    hanoi(n-1, t, to_pos,from_pos)
    
hanoi(3,1,3,2)
    


# 재귀적 이진 탐색




