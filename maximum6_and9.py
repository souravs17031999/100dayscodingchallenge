# program to return the maximum number if given some number in the range 1-10000 (excluding higher range limit), only consisting of 9's and 6's by modifying atmost one digit.

# logic is very simple as it is clear that if we go from left to right , since left digits carry more weightage, then we can understand if we change one digit wherever we get first '6' and then rest leave it as it is, then it will be the largest possible (if only one digit modification allowed.)
import math
def maximum69Number(num):
        s = str(num)
        index = 0
        result = ''
        # getting length of number
        length = math.ceil(math.log(num, 10))
        flag = 0
        while index <= length - 1:
            # if it's 9, then simply append it to result
            if s[index] == '9':
                result += s[index]
            # if it's 6, and if it's the first (which is checked by the flag) then, we append 9
            else:
                if not flag:
                    result += '9'
                    flag = 1
                # otherwise, simply append 6
                else:
                    result += '6'
            # moving forward one at a time , left to right
            index += 1
        return int(result)

print(maximum69Number(9669))
