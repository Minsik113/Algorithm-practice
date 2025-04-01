'''
날짜: 2025.04.01 20:20~20:45(25분)
링크: https://www.acmicpc.net/problem/1929
시간복잡도: O(N)

1.학습키워드
재귀+해시맵

2.문제
f(n) = f(n-1) + f(n-3) 에서 n을 입력하면 그 값이 나오게해야한다. 시간복잡도를 신경써야함.

3.어떤 문제가 있었고, 나는 어떤 시도를 했는지
재귀함수를 계속 호출하다보면 n을알기위해 n-1 n-3이 필요하고 알아야하는정보가 2배씩늘어난다
n = 3이면 f3 = f2 + f0
n = 5이면 f5 = f4 + f2
              f3 + f1 + f2
재귀만 호출하면 O(2**n) 비슷하게 나올것같은데?
봤던 값은 안보게끔 해야한다. 재귀+해시사용해서 바로 찾을 수 있게 저장한다면 재귀를 안탈 수 있다.

4.어떻게 해결했는지
재귀함수대신 O(1)알고리즘 사용

5.무엇을 새롭게 알았는지
숫자가 작아서 값을 다 넣어 둔 후에 찾는방법을 택했다. 하지만 n이 1000만을 넘어간다면 어떻게해야할까? 음.. 결국 f(n-1)과 f(n-3)에 대한 값을 알아야하므로 위풀이보다 빠를수있지만, 많이 빠르진 않을것같다. 위 풀이가 최선일지는 고민을 더 해봐야할듯.

'''
n = int(input())
ndict = [0] * 117 # 0을 제외하고 1~116사용
ndict[1] = 1
ndict[2] = 1
ndict[3] = 1
for i in range(4,117):
    ndict[i] = ndict[i-1] + ndict[i-3]

print(ndict[n])