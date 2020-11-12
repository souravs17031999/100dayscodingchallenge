# Program to compute maximum path sum from any leaf node to any leaf node in the given binary tree.
# Logic is to approach using DP =>
# TIME : 0(N)

# Use same code as for max_path_sum for any node to any node : 
# With some minor variation : 

temp = max(left, right) + root.data

if temp.left == None and temp.right == None:
   temp = max(temp, root.data)

ans = max(temp, left + right + root.data)

res = max(ans, res)



