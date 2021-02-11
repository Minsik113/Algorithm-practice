'''
# 1/22
# 문제 난이도: Gold 2
# 문제 유형: 트리, 구현
# 추천 풀이 시간: 50분
'''
# 중위순회를 이용하면 x축을 기준으로 왼쪽부터 방문한다는 특징이 있다.
# 추가적으로 Level값을 저장하여 문제를 해결하자.


#################  #################
# 나동빈
class Node:
    def __init__(self, number, left_node, right_node):
        self.parent = -1 # 루트 찾기위해 선언해둠
        self.number = number
        self.left_node = left_node
        self.right_node = right_node

def in_order(node, level):
    global level_depth, x  
    level_depth = max(level_depth, level)
    if node.left_node != -1:
        in_order(tree[node.left_node], level + 1)
    level_min[level] = min(level_min[level], x)
    level_max[level] = max(level_max[level], x)
    x += 1
    if node.right_node != -1:
        in_order(tree[node.right_node], level + 1)


n = int(input())
tree = {}
level_min = [n] # min값 저장할 것이니 제일 큰 값 넣어둠
level_max = [0] # max값 저장할 것이니 제일 작은 값 넣어둠
root = -1
x = 1
level_depth = 1

for i in range(1, n + 1):
    tree[i] = Node(i, -1, -1)
    level_min.append(n)
    level_max.append(0)

for _ in range(n):
    number, left_node, right_node = map(int, input().split(' '))
    tree[number].left_node = left_node
    tree[number].right_node = right_node
    if left_node != -1:
        tree[left_node].parent = number
    if right_node != -1:
        tree[right_node].parent = number

for i in range(1, n+1): # 루트 찾기위해. parent == -1인게 루트임
    if tree[i].parent == -1:
        root = i

in_order(tree[root], 1)

result_level = 1
result_width = level_max[1] - level_min[1] + 1
for i in range(2, level_depth+1): # 2 ~ max(level)까지
    width = level_max[i] - level_min[i] + 1
    if result_width < width:
        result_level = i
        result_width = width

print(result_level, result_width)

