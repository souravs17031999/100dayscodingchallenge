# Program to build a tree from given preorder + inorder tree or postorder + inorder tree.
# IDEA: As always, first we need to identify that this problem requires going from
# top down approach , that means preorder traversal.
# -----------------------------------------------------------------------------------------------
# Also, what we will do is to use recursive approach is , simply use something of this type
# buildTree(inorder, preorder, instr, inend)
# obviously, base case will be when start > end, because start will be ++, end will be --
# so, now, we know what preorder first element is always root of the tree, and after that
# identification, we search for that particular element in  the inorder array, as we know
# that inorder gives us left subtree and right subtree elements.
# So, we keep a pointer for preorder array (which will be static as we donot need to backtrack to any earlier visted node)
# so in recursive call, the value of pointer should not be initialised again, and should go on to next element in preorder arr
# Now, in this way, we build the root by picking the preorder element and then searching for it in inorder array,
# Then call recursively, for building left part and right part by using this found index in the inorder array.
# as the element at idx - 1 will be left child, and idx + 1 will be right child for the tree build.
# AS WE ARE PROCESSING EACH preorder ARRAY ELEMENT AND FOR EVERY ELEMENT, WE SEARCH IT IN inorder ARRAY,
# TIME : 0(N^2), SPACE : 0(N).
# CAN WE DO BETTER THAN THIS ?
# Finding this index in inorder can also be done using binary search which will reduce the time complexity to 0(N * log(N)).
# Can we do more better than this ?
# ------------------------------------------------------------------------------------------------
# We can observe the main bottleneck of the algorithm is finding this element of preorder in the inorder array.
# So, we can simply maintain a hashmap (dict) which saves its index so that we already know what it's index is given
# the element as its key and index is its value.
# Time : 0(N), SPACE : 0(N).
# -------------------------------------------------------------------------------------------------
# We can take example for follwoing tree and visualize stack call :
#            1
#          /  \
#        2     3
#       /  \
#      4    5
# --------------------------------
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

from collections import deque
# function for level order traversal for binary tree
def levelOrder(root):

    if not root:
        return

    queue = deque([])
    queue.append(root)

    while queue:

        temp = queue.popleft()
        print(temp.data, end = " ")

        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)

# FIRST approach (RECURSIVE) , 0(N^2)
# function to search the index of element in inorder array
def search(arr, start, end, ele):
    for i in range(start, end + 1):
        if arr[i] == ele:
            return i



# Here, we avoid use of static variable as a ptr, and simply modify the preorder by
# popping off from the start, and hence now i also don't need start and end.
# Also, above instead of above search we are using list.index() which is similar to above
# function .

def buildTree(inorder, preorder):

    if len(inorder) and len(preorder):

        root_val = preorder.pop(0)
        root = Node(root_val)


        idx = inorder.index(root_val)

        root.left = buildTree(inorder[:idx], preorder)
        root.right = buildTree(inorder[idx + 1:], preorder)

        return root


# ----------------------------------------------------------
# SECOND OPTIMIZED APPROACH (RECURSIVE) USING HASHING

def buildTreeFast(inorder, preorder, map):

    if len(inorder) and len(preorder):

        root_val = preorder.pop()
        root = Node(root_val)


        idx = map[root_val]

        root.left = buildTreeFast(inorder[:idx], preorder, map)
        root.right = buildTreeFast(inorder[idx + 1:], preorder, map)

        return root


# We are using map to build a dict, of inorder elements so that we do not have to search for it.
# we also reverse the preorder beforehand so that, we can pop in 0(1) so overall we are popping off from
# start of preorder elements but now in 0(1).
def buildTreeMAP(inorder, preorder):
    n = len(inorder)
    TreeMap = {}
    for i in range(n):
        TreeMap[inorder[i]] = i

    preorder = preorder[::-1]

    return buildTreeFast(inorder, preorder, TreeMap)


# driver test function
if __name__ == '__main__':
    inorder, preorder =  [9, 3, 15, 20, 7], [3, 9, 20, 15, 7]
    root = buildTreeMAP(inorder, preorder)
    levelOrder(root)
