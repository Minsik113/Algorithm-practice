'''
# 1/22
# 문제 난이도: Silver 1
# 문제 유형: 트리, 구현
# 추천 풀이 시간: 20분
'''


################  ###############
# 나동빈
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def preorder_tree(node):
    print(node.data, end='')
    if node.left_node != '.':
        preorder_tree(tree[node.left_node])
    if node.right_node != '.':
        preorder_tree(tree[node.right_node])

def inorder_tree(node):
    if node.left_node != '.':
        inorder_tree(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != '.':
        inorder_tree(tree[node.right_node])

def postorder_tree(node):
    if node.left_node != '.':
        postorder_tree(tree[node.left_node])
    if node.right_node != '.':
        postorder_tree(tree[node.right_node])
    print(node.data, end='')

n = int(input())
tree = {} # dict()
for _ in range(n):
    root, left_node, right_node = input().split(' ')
    tree[root] = Node(root, left_node, right_node)

preorder_tree(tree['A'])
print()
inorder_tree(tree['A'])
print()
postorder_tree(tree['A'])