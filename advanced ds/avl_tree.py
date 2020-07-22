class Node(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1

class avl_tree(object): 
  
    def insert(self, root, key): 
      
        if not root: 
            return Node(key) 
        elif key < root.val: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 
  

        root.height = 1 + max(self.get_height(root.left), 
                           self.get_height(root.right)) 
  
        balance = self.get_balance(root) 
  

        if balance > 1 and key < root.left.val:
            print(root.val)
            return self.right_rotate(root) 
  
        if balance < -1 and key > root.right.val:
            print(root.val)
            return self.left_rotate(root) 
  
        if balance > 1 and key > root.left.val: 
            root.left = self.left_rotate(root.left)
            print(root.val)
            return self.right_rotate(root) 
  
        if balance < -1 and key < root.right.val: 
            root.right = self.right_rotate(root.right)
            print(root.val)
            return self.left_rotate(root) 
  
        return root 
  
    def left_rotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self.get_height(z.left), 
                         self.get_height(z.right)) 
        y.height = 1 + max(self.get_height(y.left), 
                         self.get_height(y.right)) 
  
        return y 
  
    def right_rotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        y.right = z 
        z.left = T3 
  
        z.height = 1 + max(self.get_height(z.left), 
                        self.get_height(z.right)) 
        y.height = 1 + max(self.get_height(y.left), 
                        self.get_height(y.right)) 
  
        return y 
  
    def get_height(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def get_balance(self, root): 
        if not root: 
            return 0
  
        return self.get_height(root.left) - self.get_height(root.right) 
    
    def delete(self, root, key): 
  
        if not root: 
            return root 
  
        elif key < root.val: 
            root.left = self.delete(root.left, key) 
  
        elif key > root.val: 
            root.right = self.delete(root.right, key) 
  
        else: 
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 
  
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
  
            temp = self.min_value(root.right) 
            root.val = temp.val 
            root.right = self.delete(root.right, temp.val) 
  

        if root is None: 
            return root 
  
        root.height = 1 + max(self.get_height(root.left), 
                            self.get_height(root.right)) 
  
        balance = self.get_balance(root) 
  
        if balance > 1 and self.get_balance(root.left) >= 0: 
            print(root.val)
            return self.right_rotate(root) 
  
        if balance < -1 and self.get_balance(root.right) <= 0:
            print(root.val)
            return self.left_rotate(root) 
  
        if balance > 1 and self.get_balance(root.left) < 0: 
            root.left = self.left_rotate(root.left)
            print(root.val)
            return self.right_rotate(root) 
  
        if balance < -1 and self.get_balance(root.right) > 0: 
            root.right = self.right_rotate(root.right)
            print(root.val)
            return self.left_rotate(root) 
  
        return root     
        
    def min_value(self, root): 
        if root is None or root.left is None: 
            return root 
  
        return self.get(root.left) 
        
    def pre_order(self, root): 
  
        if not root: 
            return
  
        print("{0} ".format(root.val), end="") 
        self.pre_order(root.left) 
        self.pre_order(root.right) 
    def post_order(self, root): 
  
        if not root: 
            return
  
        self.post_order(root.left) 
        self.post_order(root.right)    
        print("{0} ".format(root.val), end="") 
    def in_order(self, root): 
  
        if not root: 
            return
  
        self.in_order(root.left) 
        print("{0} ".format(root.val), end="") 
        self.in_order(root.right)    
        
  
  
t = avl_tree() 
root = None

n = int(input())
while(n):
    p = list(input().strip().split())
    if p[0] == 'i':
        root = t.insert(root, int(p[1]))
    else:
        root = t.delete(root, int(p[1]))
    n -= 1

t.pre_order(root)
print()
t.in_order(root)
print()
t.post_order(root)