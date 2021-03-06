# IN INTERVIEW, LOOK OUT FOR PATTERNS  :
* Two pointer technique (generally after sorting) :
> CONVERGING TOWARDS THE CENTER =>  WHILE START < END
> DIVERGING AWAY FROM CENTER (EXPANDING FROM CENTER) => WHILE START >= 0 AND END < LENGTH

* Hashing : HASHMAP/HASHTABLE     
* Bitsmasking (XOR TRICKS)   
* Window sliding (MAX/MIN, SUM, PRODUCT, XOR OF K SIZED WINDOW FOR MAXIMUM, MINIMUM, LONGEST, SMALLEST) :
> STATIC SIZED WINDOW SLIDING : FIXED WINDOW SIZE DURING WHOLE TRAVERSAL (USUALLY SIMULATED BY TWO POINTERS START, END)  
> DYNAMIC SIZED WINDOW SLIDING : VARIABLE SIZING WINDOW, EXPAND FROM RIGHT SIDE, SHRINK FROM LEFT SIDE.
> DYNAMIC SIZED WINDOW + AUX. DS : VARIABLE SIZING WINDOW + SOME KIND OF HASHMAP/HASHTABLE    
> IMPORTANT : IF we want to answer some queries for every window : then use Deque/queue based approach (not a single answer)   

* Modified binary search (keep searching even if value is found by including other conditions)
* Prefix cumulative sum array (for range queries)
```
prefix[i] = arr[i] + prefix[i - 1]
```
* OTHER ADVANCED TECHNIQUES FOR RANGE QUERIES : SEGMENT TREES, FENWICK TREES.
