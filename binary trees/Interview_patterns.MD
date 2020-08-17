# FOR INTERVIEW PATTERNS :
* TOP DOWN APPROACH :
## Preorder/ level order traversal/ ANY DFS ITERATIVE
## Normal DAC recursive approach
## Direct recursive relations
* BOTTOM UP APPROACH :
## Postorder
## Pair logic (returning multiple values from node going bottom up)
* General tips :
* Complexity reduces from 0(N^2) => 0(N) by using bottom up approach.
* Also, sometimes hashmaps, deque, queue can reduce Complexity.
* In any recursive calls, we pass one of the args in the calls whom we don't intend to change in the every recursive call,
* so, we pass it by reference by sending list[element] in the intial args.
* If doing iterative approach and need to go back up, hashmaps storing back pointers (parent) is really helpful
(True for trees and graphs).    
## Iterative approach :   
* Usually this takes more space due to stack/queue/deque but this is pretty easy to think in terms of BFS approach (often coupled with None pointer delimiter logic) 
* We can use a queue with BFS coupled with HashMap sorting based on keys efficient for vertical order/bottom order otherwise we can also implement our own MAP as python doesn;t
support inbuild dict sorted.
