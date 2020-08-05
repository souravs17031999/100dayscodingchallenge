# Program for computing maximum possible equal sum in the three stacks.
# -----------------------------------------------------------------------------
# So, we have to find maximum sum but it should be equal in all the three stacks.
# So, we can think about greedy approach where we can try to minimize the elements of stack
# containing maximum sum among the three when we don't have equal sum in the stack , because we
# can only remove the top item from the stack, so we can try to remove the items one by one
# from max sum containing stack to be made equal to sum for other two.
# If at any point of time, if sums are equal, then we are good. This is the max. sum possible.
# -------------------------------------------------------------------------------------------
# stack1[] = { 3, 10}
#  stack2[] = { 4, 5 }
#  stack3[] = { 2, 1 }
# Lets's say in the above ex. we have sum(stack1) : 13, sum(stack2) : 9, sum(stack3) : 3.
# Now, for making sum equal, we will remove "3" from stack 1 as this is having max sum,
# hence, now new updated sum is 10, again it's not same,
# now, stack1 : [10], stack2 : [4, 5], stack3 : [2, 1]
# now , remove "10" from stack1 again, and now it is empty.
# since it is now 0 sum for stack1, it is impossible for other two making upto 0, unless we remove
# all the elements from other two, which in this case is true.
# So, output : 0.
# ----------------------------------------------------------------------------------------------
# TIME : 0(N1 + N2 + N3), WHERE N(i) is the length of ith stack.
# -------------------------------------------------------------------------------------

def compute_max_sum(stack1, stack2, stack3, n1, n2, n3):

    sum1, sum2, sum3 = sum(stack1), sum(stack2), sum(stack3)
    # since, here according to the question, stack removal is allowed from left side due to array repr
    # so, we will maintain the top by a pointer and keep incrementing it.
    # otherwise removal from left is a costly operation in lists.
    top1, top2, top3 = 0, 0, 0
    while 1:

        if top1 == n1 or top2 == n2 or top3 == n3:
            return 0

        if sum1 == sum2 == sum3:
            return sum1

        if sum1 > sum2 and sum1 > sum3:
            pop_value = stack1[top1]
            sum1 -= pop_value
            top1 += 1

        elif sum2 > sum1 and sum2 > sum3:
            pop_value = stack2[top2]
            sum2 -= pop_value
            top2 += 1

        elif sum3 > sum1 and sum3 > sum2:
            pop_value = stack3[top3]
            sum3 -= pop_value
            top3 += 1

stack1 = [ 3, 2, 1, 1, 1 ]
stack2 = [ 4, 3, 2 ]
stack3 = [ 1, 1, 4, 1 ]

n1 = len(stack1)
n2 = len(stack2)
n3 = len(stack3)

print(compute_max_sum(stack1, stack2, stack3, n1, n2, n3))
