class tree_node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None


class splay_tree:
    def __init__(self):

        self.root=None

    def insert(self,key):
        count = 0
        if not self.root:
            self.root=tree_node(key)
            return count 

        self.root=self.splaying(self.root,key)
        count += 1 
        if key==self.root.key:
            self.root

        elif key<self.root.key:     
            node=tree_node(key)
            node.right=self.root    
            node.left=self.root.left
            self.root.left=None
            self.root=node

        else:
            node=tree_node(key)
            node.left=self.root
            node.right=self.root.right 
            self.root.right=None
            self.root=node
        return count     


    def find(self,key):
        count = 0
        self.root=self.splaying(self.root,key)
        count += 1
        if self.root.key==key:
            return count 
        return count
        


    def __contains__(self,key):

        return self.find(key)!=None



    def remove(self,key):
        count = 0
        if not self.root:
            return count 

        self.root=self.splaying(self.root,key)
        count += 1 
        if self.root.key!=key:
            return count 

        else:  

            if self.root.left==None:
                self.root=self.root.right

            else: 
                righttree=self.root.right
                self.root=self.splaying(self.root.left,key)  
                count += 1 
                self.root.right=righttree
        return count        

    def splaying(self,node,key):

        if not node:
            return None

        if key==node.key:
            return node

        if key<node.key:
            if node.left==None:
                return node

            if key<node.left.key:
                node.left.left=self.splaying(node.left.left,key) 
                node=self.rotateRight(node)

            elif key>node.left.key:
                node.left.right=self.splaying(node.left.right,key)
                if node.left.right:
                    node.left=self.rotateLeft(node.left)

            if node.left:
                return self.rotateRight(node)

            return node


        elif key>node.key:
            if node.right==None:
                return node

            if key<node.right.key:
                node.right.left=self.splaying(node.right.left,key)
                if node.right.left:
                    node.right=self.rotateRight(node.right)

            elif key>node.right.key:
                node.right.right=self.splaying(node.right.right,key)
                node=self.rotateLeft(node)

            if node.right:
                return self.rotateLeft(node)

            return node


    def rotateLeft(self,node):  
        if not node:
            return None

        child=node.right

        if not child:
            return node

        node.right=child.left
        child.left=node

        return child


    def rotateRight(self,node): 

        if not node:
            return None

        child=node.left

        if not child:
            return node

        node.left=child.right

        child.right=node

        return child
    
    def __pre_order_helper(self, node):
        if node != None:
            print(f"{node.key} ", end = "")
            self.__pre_order_helper(node.left)
            self.__pre_order_helper(node.right)
    def __in_order_helper(self, node):
        if node != None:
            self.__in_order_helper(node.left)
            print(f"{node.key} ", end = "")
            self.__in_order_helper(node.right)
            
    def __post_order_helper(self, node):
        if node != None:
            self.__post_order_helper(node.left)
            self.__post_order_helper(node.right)
            print(f"{node.key} ", end = "")
            
    def preorder(self):
        self.__pre_order_helper(self.root)
    
    
    def inorder(self):
        self.__in_order_helper(self.root)
    
    def postorder(self):
        self.__post_order_helper(self.root)
    

t = splay_tree() 
n = int(input())
count = 0
count_insert, count_find, count_remove = 0, 0, 0
while(n):
    p = list(input().strip().split())
    if p[0] == 'i':
        count = t.insert(int(p[1]))
        count_insert += count 
        
    elif p[0] == 's':
        count = t.find(int(p[1]))
        count_find += count
    else:
        count = t.remove(int(p[1]))
        count_remove += count
    n -= 1
    
t.preorder()
print()
t.inorder()
print()
t.postorder()
print()
print(count_insert + count_find + count_remove)