class Node:
	def  __init__(self, data):
		self.data = data
		self.parent = None
		self.left = None
		self.right = None

class splay_tree:
	def __init__(self):
		self.root = None

			
	def __search_tree_helper(self, node, key):
		if node == None or key == node.data:
			return node

		if key < node.data:
			return self.__search_tree_helper(node.left, key)
		return self.__search_tree_helper(node.right, key)

	def __delete_node_helper(self, node, key):
		x = None
		t = None 
		s = None
		while node != None:
			if node.data == key:
				x = node

			if node.data <= key:
				node = node.right
			else:
				node = node.left

		if x == None:
			return
		
		zig, zig_zig, zig_zag = self.__splay(x)
		if x.right != None:
			t = x.right
			t.parent = None
		else:
			t = None

		s = x
		s.right = None
		x = None

		if s.left != None:
			s.left.parent = None

		self.root, zig_n, zig_zig_n, zig_zag_n = self.__join(s.left, t)
		s = None
		return zig + zig_n, zig_zig + zig_zig_n, zig_zag + zig_zag_n

	def __left_rotate(self, x):
		y = x.right
		x.right = y.left
		if y.left != None:
			y.left.parent = x

		y.parent = x.parent
		if x.parent == None:
			self.root = y
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y
		y.left = x
		x.parent = y

	def __right_rotate(self, x):
		y = x.left
		x.left = y.right
		if y.right != None:
			y.right.parent = x
		
		y.parent = x.parent;
		if x.parent == None:
			self.root = y
		elif x == x.parent.right:
			x.parent.right = y
		else:
			x.parent.left = y
		
		y.right = x
		x.parent = y

	def __splay(self, x):
		zig = 0
		zig_zig = 0
		zig_zag = 0	
		while x.parent != None:
			if x.parent.parent == None:
				if x == x.parent.left:
					self.__right_rotate(x.parent)
					zig += 1
				else:
					self.__left_rotate(x.parent)
					zig += 1
			elif x == x.parent.left and x.parent == x.parent.parent.left:
				self.__right_rotate(x.parent.parent)
				self.__right_rotate(x.parent)
				zig_zig += 1
			elif x == x.parent.right and x.parent == x.parent.parent.right:
				self.__left_rotate(x.parent.parent)
				self.__left_rotate(x.parent)
				zig_zig += 1
			elif x == x.parent.right and x.parent == x.parent.parent.left:
				self.__left_rotate(x.parent)
				self.__right_rotate(x.parent)
				zig_zag += 1
			else:
				self.__right_rotate(x.parent)
				self.__left_rotate(x.parent)
				zig_zag += 1
		return zig, zig_zig, zig_zag		
				
	def __join(self, s, t):
		if s == None:
			return t

		if t == None:
			return s

		x = self.maximum(s)
		zig, zig_zig, zig_zag = self.__splay(x)
		x.right = t
		t.parent = x
		return x, zig, zig_zig, zig_zag

	def __pre_order_helper(self, node):
		if node != None:
			print(f"{node.data} ", end = "")
			self.__pre_order_helper(node.left)
			self.__pre_order_helper(node.right)

	def __in_order_helper(self, node):
		if node != None:
			self.__in_order_helper(node.left)
			print(f"{node.data} ", end = "")
			self.__in_order_helper(node.right)

	def __post_order_helper(self, node):
		if node != None:
			self.__post_order_helper(node.left)
			self.__post_order_helper(node.right)
			print(f"{node.data} ", end = "")


	def preorder(self):
		self.__pre_order_helper(self.root)


	def inorder(self):
		self.__in_order_helper(self.root)

	def postorder(self):
		self.__post_order_helper(self.root)


	def search_tree(self, k):
		zig, zig_zig, zig_zag = 0, 0, 0
		x = self.__search_tree_helper(self.root, k)
		if x != None:
			zig, zig_zig, zig_zag = self.__splay(x)
		return zig, zig_zig, zig_zag	

	def minimum(self, node):
		while node.left != None:
			node = node.left
		return node

	def maximum(self, node):
		while node.right != None:
			node = node.right
		return node

	def successor(self, x):
		if x.right != None:
			return self.minimum(x.right)

		y = x.parent
		while y != None and x == y.right:
			x = y
			y = y.parent
		return y

	def predecessor(self, x):
		if x.left != None:
			return self.maximum(x.left)

		y = x.parent
		while y != None and x == y.left:
			x = y
			y = y.parent
		return y

	def insert(self, key):
		node =  Node(key)
		y = None
		x = self.root

		while x != None:
			y = x
			if node.data < x.data:
				x = x.left
			else:
				x = x.right

		node.parent = y
		if y == None:
			self.root = node
		elif node.data < y.data:
			y.left = node
		else:
			y.right = node
		zig, zig_zig, zig_zag = self.__splay(node)
		return zig, zig_zig, zig_zag
		

	def delete_node(self, data):
		return self.__delete_node_helper(self.root, data)

	def pretty_print(self):
		self.__print_helper(self.root, "", True)


t = splay_tree() 
n = int(input())
count_zig, count_zig_zig, count_zig_zag = 0, 0, 0
while(n):
    p = list(input().strip().split())
    if p[0] == 'i':
        zig, zig_zig, zig_zag = t.insert(int(p[1]))
        count_zig += zig
        count_zig_zig += zig_zig
        count_zig_zag += zig_zag
    elif p[0] == 's':
        zig, zig_zig, zig_zag = t.search_tree(int(p[1]))
        count_zig += zig
        count_zig_zig += zig_zig
        count_zig_zag += zig_zag
    else:
        zig, zig_zig, zig_zag = t.delete_node(int(p[1]))
        count_zig += zig
        count_zig_zig += zig_zig
        count_zig_zag += zig_zag
    n -= 1


t.preorder()
print()
t.inorder()
print()
t.postorder()
print()
print(count_zig)
print(count_zig_zig)
print(count_zig_zag)