# Program to check if given two rectangles overlap.
#
#                l2 ___________________
#                  |                  |
#   l1 ------------|__________________| r2
#     |                        |        
#     |                        |
#     |________________________| r1
#
#  Return : True
# -------------------------------------------------------------------------------------------------------
# so, let's see when the rectangles don;t overlap : (we have to focus on extremes of dimensions)
# When one of the either rectangle out of overlap in horizontal direction or in vertical direction 
#
# So, let's check in horizontal direction : 
#
#    l1  ______________        l2 ____________
#       |             |          |           |            r1.x < l2.x [first rect. is left to second rect.]
#       |_____________| r1       |___________| r2         
#       
#
#     l2 ______________        l1 ____________
#       |             |          |           |            l1.x < r2.x [first rect. is right to second rect.]
#       |_____________| r2       |___________| r1         
#    
#
#  now, let's check in vertical direction  :
#    
#     l1 ______________
#       |              |   
#       |______________| r1 
#                                        r1.y > l2.y [first rect. is above second rect.]
#     l2 ______________
#       |             |  
#       |_____________| r2
#
#
#   l2   ______________
#       |              |   
#       |______________| r2
#                                        r2.y > l1.y [first rect. is below second rect.]
#     l1 ______________
#       |             |  
#       |_____________| r1
#
# ------------------------------------------------------------------------------------------------------
# TIME : 0(1), SPACE : 0(1)

def check_if_overlap(l1, r1, l2, r2):
    
    if l1[0] >= r2[0] or r1[0] <= l2[0]:  # if one of the rectangles goes outside one of the other, no overlaps
        return False 
    
    if r2[1] >= l1[1] or r1[1] >= l2[1]: 
        return False 
    
    return True

# all coordinates are tuples of (x, y)
print(check_if_overlap((0, 10), (10, 0), (5, 5), (15, 0)))
