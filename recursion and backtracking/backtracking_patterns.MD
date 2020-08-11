# Three things to keep in mind always solving backtracking problems :
## * CHOICE : what do we do , we place item/ we remove the item / anything like in sudoku, n-queens etc....,
## searching exhaustively for all possibilities.
## * CONSTRAINTS : what is the way to validate the solution if it is correct or not. How do we tell if it is correct placement ?
## * GOAL : Base cases which decide we have reached our solution , or if we are out of bound.

# General template  :
```

def solve(row, col):
    if col == board[row].length{
      base cases check and return answer
    }

    for val from 1 : 9 => {
      board[row][col] = value
      if validplacement(row, col....){
        if solve(row, col + 1, board){
          return true
        }
        board[row][col] = 0
      }
    }

```

# So, we keep placing, validation and undoing the wrong path and recurse for other path.
