# Program to define the custom data structure -> disjoint sets.
# This would help in grouping all the other individual sets (single nodes or element),
# and all elements in the group be represented by single root node.
# There are two ways of implemeneting this :
# -----------------------------------------------------------------------------
# EX. 10 individuals : a, b, c, d, e, f, g, h, i, j
# if there are some relationships, to be defined,
# a <> b
# b <> d
# c <> f
# c <> i
# j <> e
# g <> j
# We can group all the above elements based on the above relationships
# -----------------------------------------------------------------------------
# Now, finding if element belongs in which representative set (by root node),
# can be inefficient because we have to traverse whole to the root node.
# -----------------------------------------------------------------------------
# So, technique of Path compression has to be applied so that every element while
# setting parent node for the element i , we can set all the nodes to be pointed to
# parent of i (root node).
# So, almost all of the nodes will be pointing directly towards the root node.
# It can be really efficient for queries, to say if element belongs to which group.
# it is on average 0(1) time.
# -----------------------------------------------------------------------------
#
#
#                   1        40
#                    \      /
#                 2 -- 4 -- 20 -- 100
#                    /      \
#                  10        50
#
# -----------------------------------------------------------------------------
# ALso, Union operation will be optimized by calculating rank[i] array which contains height of the traverse
# and attempt will be reduce the height of the tree as much as possible by appending greater rank as child of
# lower rank.
# -----------------------------------------------------------------------------
# Useful for graph algorithms like MST krushkal's, and other social networking, friendships, or representing
# all other graph type relationships.

class disjoint:

    def __init__(self, V):

        self.rank  = [1] * V
        self.parent = [i for i in range(V)]

    def find(self, x):

        # if x is not the parent of itself , then x is not the representative of this set
        if self.parent[x] != x:

            # so we recursively call find on its parent and move i's node directly
            # under the representative of this set
            self.parent[x] = self.find(self.parent[x])

        # else return the parent
        return self.parent[x]

    def union(x, y):

        # Find current sets of x and y
        xset = self.find(x)
        yset = self.find(y)

        # If they are already in same set
        if xset == yset:
            return

        # Put smaller ranked item under
        # bigger ranked item if ranks are
        # different
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset

        # If ranks are same, then move y under
        # x (doesn't matter which one goes where)
        # and increment rank of x's tree
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset

        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1

# driver test function
if __name__ == '__main__':

    ds = disjoint(5)
