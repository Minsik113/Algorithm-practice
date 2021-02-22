'''
1/ 작년등수 

1) 작년등수와 나란한 순서로 나온게 있다면 "IMPOSSIBLE"
2) 정답이 여러개라면 "?"
3) 정답 한 개면 출력

-> m개 쭉입력받는다. (a,b) b는 a의 뒤에 나와야한다.
graph[b] = a  b가나오려면 a가 나와야함
indegree[b] += 1

'''

# 테스트 수
test = int(input())

for _ in range(test):
    n = int(input())
    lastyear = list(map(int, input().split()))
    m = int(input())
    graph = [[] for _ in range(n+1)] # 1~n
    indegree = [0] * (n+1) # 1~n

    for _ in range(m):
        a, b = map(int,input().split()) # a - b 순서임
        # a가 b앞에있다.
        graph[a].append(b)
        indegree[b] += 1

    print(graph)
    print(indegree)

