'''

'''
class Node:
    def __init__(self, data, left_node, right_node) -> None:
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def preorder(node): # root left right
    print(tree[node].data, end='')
    if tree[node].left_node != '.':
        preorder(tree[node].left_node)
    if tree[node].right_node != '.':
        preorder(tree[node].right_node)

def inorder(node): # left root right
    if tree[node].left_node != '.':
        inorder(tree[node].left_node)
    print(tree[node].data, end='')
    if tree[node].right_node != '.':
        inorder(tree[node].right_node)

def postorder(node): # left right root
    if tree[node].left_node != '.':
        postorder(tree[node].left_node)
    if tree[node].right_node != '.':
        postorder(tree[node].right_node)
    print(tree[node].data, end='')

n = int(input())
tree = dict()
for _ in range(n):
    data, left, right = input().split()
    tree[data] = Node(data, left, right)

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()


# '''
# 노드 
#     data
# left    right
# '''
# class Node:
#     def __init__(self, data, left, right):
#         self.data = data
#         self.left = left
#         self.right = right

# def preorder(node):
#     print(node.data, end= '')
#     if node.left != '.':
#         preorder(tree[node.left])
#     if node.right != '.':
#         preorder(tree[node.right])

# def inorder(node):
#     if node.left != '.':
#         inorder(tree[node.left])
#     print(node.data, end= '')
#     if node.right != '.':
#         inorder(tree[node.right])

# def postorder(node):
#     if node.left != '.':
#         postorder(tree[node.left])
#     if node.right != '.':
#         postorder(tree[node.right])
#     print(node.data, end= '')

# n = int(input())
# tree = dict()
# for _ in range(n):
#     data, left, right = input().split()
#     tree[data] = Node(data, left, right)

# preorder(tree['A'])
# print()
# inorder(tree['A'])
# print()
# postorder(tree['A'])
# print()
