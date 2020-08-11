## The overall approach should be if we can divide the search space recursively and compute the solution from left half
## side, compute the solution from right half space and finally combine all solutions and return it.
# General template :

```
DAC(a, i, j){

     if small_enough_to_be_solved(a, i, j){
       return solution(a, i, j)
     }
     else{
       m = divide(a, i, j)
       b = DAC(a, i, mid)
       c = DAC(a, mid + 1, j)
       d = combine(b, c)
   }
    return d
}
```
