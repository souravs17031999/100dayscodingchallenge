# Program for cloning the binary tree.
# Logic is same as other cloning problems, using the hashMaps, we store the references in the key:value :: {root : Node(root.data)}

class Node:
    def __init__(self, x, left=None, right=None, random=None):
        self.data = x
        self.left = left
        self.right = right 
        self.random = random 

def preorder(root):
    
    if root == None:
        return 
    
    preorder(root.left)
    preorder(root.right)
    print(root.data, end = "->")
    
def clone_random(root, map):
    
    if map.get(root) is None:
        return
    
    map.get(root).random = map.get(root.random)
    clone_random(root.left, map)
    clone_random(root.right, map)
    

def clone_left_right(root, map):
    
    if root == None:
        return 
    
    map[root] = Node(root.data)
    map[root].left = clone_left_right(root.left, map)
    map[root].right = clone_left_right(root.right, map)
    
    return map[root]

def clone_tree(root):
    if root == None:
        return 
    
    map = {}
    clone_left_right(root, map)
    clone_random(root, map)
    
    return map[root]

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    root.random = root.right.left.random
    root.left.left.random = root.right
    root.left.right.random = root
    root.right.left.random = root.left.left
    root.random = root.left

    print("Preorder traversal of the original tree:")
    preorder(root)

    clone = clone_tree(root)
    print()
    print("Preorder traversal of the clone tree:")
    preorder(clone)
