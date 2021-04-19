class Node:
    def __init__(self, value=None, l_value=None, r_value=None):
        self.value = value
        self.left = l_value
        self.right = r_value

class Tree:
    def __init__(self, root=None):
        self.root = root
    
    def push(self, value):
        node = Node(value = value)
        tempNode = self.root

        if self.root is None:
            self.root = node
            return
        
        else:
            ptrNode = self.root
            while ptrNode is not None:
                tempNode = ptrNode
                if node.value < ptrNode.value:
                    ptrNode = ptrNode.left
                else:
                    ptrNode = ptrNode.right

if __name__ == "__main__":
    tree = Tree()
    tree.push(100)
    tree.push(40)
