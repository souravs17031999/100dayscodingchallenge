# program for checking if its a straight line or not , given a set of coordinates
# IDEA: logic is to calculate the slope of first two coordinates and then check slope of every other point, if all are same then we can form straight line passing through all of them otherwise not.

from sys import stdin, stdout
def check_straight(coordinates):
    # setting the intial coordinates for finding slope
    x1, y1, x2, y2 = coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1]
    for x, y in coordinates:
        if (y - y1)*(x2 - x1) != (y2 - y1)*(x - x1):   # for calculating slope using product form of slope formula to avoid zero divison error
            return False
    return True

# tests
assert check_straight([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == True
assert check_straight([[1,1],[1,2],[3,4],[4,5],[5,6],[7,7]]) == False
# main function 
if __name__ == '__main__':
    coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    stdout.write(str(check_straight(coordinates)))
