# Using deque to represent SNAKE because it will be most logically correct and we can use HashSet to make list of all visited positions.
# Given, height and width of the window screen and food is a list of positions [x, y].

from collections import deque 
from sys import stdin, stdout
class Snake:
    
    def __init__(self, height, width, food):
        self.height = height
        self.width = width
        self.food = food
        self.body = deque()
        self.body.append((0, 0))
        self.food_idx = 0
        self.score = 0
        self.visited = set()
        self.visited.add((0, 0))
        print("Snake starting from (0, 0)...")
        
    def move(self, direction):
        # if no move yet 
        if self.score == -1 or direction == ' ':
            return 0
        
        # take the move 
        curr_row, curr_col = self.body[0][0], self.body[0][1]
        
        if direction == 'U':
            curr_row -= 1
            print("Snake moving towards up...")
        elif direction == 'D':
            curr_row += 1
            print("Snake moving towards down...")
        elif direction == 'R':
            curr_col += 1
            print("Snake moving towards right...")
        elif direction == 'L':
            curr_col -= 1
            print("Snake moving towards left...")
        
        #self.visited.remove(self.body[-1])
        # check if game over due to out of bounds 
        if curr_row < 0 or curr_row > self.height or curr_col < 0 or curr_col > self.width:
            print("GAME OVER !")
            return -1
        
        # update the visited set and body deque 
        
        
        # check if this move leads to food 
        if self.food_idx < len(self.food) and curr_row == self.food[self.food_idx][0] and curr_col == self.food[self.food_idx][1]:
            print("FOOD FOUND !")
            self.score += 1
            self.food_idx += 1
            self.body.appendleft((curr_row, curr_col))
            return self.score
        
        # if not leads to food, then we need to remove last pos visited
        
        self.body.pop()
        self.body.appendleft((curr_row, curr_col))
        return self.score
    
    def pretty_print(self):
        print(self.body)
        
        
if __name__ == '__main__':
    
    snake = Snake(2, 3, [[1, 2], [0, 1]])
    print(snake.move('D'))
    print(snake.move('R'))
    print(snake.move('R'))
    print(snake.move('U'))
    print(snake.move('L'))
    print(snake.move('L'))
    print(snake.move('L'))
    snake.pretty_print()
