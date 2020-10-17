# IDEAS FOR STRING INTERVIEW PATTERNS :    
* HashTable using array indices for 256 chars (total ascii letters)   / 26 CHARS (IF ONLY LOWERCASE)     
* Two pointers technique (start and end until they collide or expand from middle)    
* Tehchniques for extracting actual digit from string sigit : ord('1') - ord('0')           
* Two pointers for multiple strings comparison KMP, robin-karp, boyer-moore
(Important to know underlying strategies) !    
* Window sliding (MAX/MIN, SUM, PRODUCT, XOR OF K SIZED WINDOW FOR MAXIMUM, MINIMUM, LONGEST, SMALLEST) :
> STATIC SIZED WINDOW SLIDING : FIXED WINDOW SIZE DURING WHOLE TRAVERSAL (USUALLY SIMULATED BY TWO POINTERS START, END)   
> DYNAMIC SIZED WINDOW SLIDING : VARIABLE SIZING WINDOW, EXPAND FROM RIGHT SIDE, SHRINK FROM LEFT SIDE.   
> DYNAMIC SIZED WINDOW + AUX. DS : VARIABLE SIZING WINDOW + SOME KIND OF HASHMAP/HASHTABLE          
* TIP : DON'T USE STRING FOR MODIFICATIONS, FIRSTLY BREAK IT INTO LIST, THEN APPLY MODIFICATIONS AND FINALLY WHILE RETURNING JOIN IT.
* TRIES : FOR LIST OF STRINGS QUESTIONS LIKE MATCHING, PREFIX, SUFFIX ETC..

> Template for sliding window approach  :   
* we need two variables "start" and "end" to control the sliding of window.   
```   
start = 0   
count = 0    
for i in range(len(s)):    
   count += 1    
   if count == 3:    
       print(s[start : i + 1])    
       start += 1    
       count -= 1   
   print()   
```    
