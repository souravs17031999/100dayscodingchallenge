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
> IMPORTANT : IF we want to answer some queries for every window : then use Deque/queue based approach (not a single answer)     

* TIP : DON'T USE STRING FOR MODIFICATIONS, FIRSTLY BREAK IT INTO LIST, THEN APPLY MODIFICATIONS AND FINALLY WHILE RETURNING JOIN IT.
* TRIES : FOR LIST OF STRINGS QUESTIONS LIKE MATCHING, PREFIX, SUFFIX ETC..

> Template for sliding window approach (static size) :   
* we need two variables "start" and "end" to control the sliding of window, k is size of window.   
```   
start = 0   
count = 0    
for end in range(len(s)):    
   count += 1    
   if count == k:    
       print(s[start : end + 1])    
       start += 1    
       count -= 1   
   print()   
```      

> Template for sliding window approach (static size + hashing) :    
* Remember to use static array of size 26 / 128 for strings problems :      
```   
map = [0] * 26/128     
start = 0     
count = 0    
for end in range(len(s)):    
   count += 1    
   
   map[ord(s[i]) - ord('a')] += 1
   if count == k:       
       // other logic    
       
       map[ord(s[start]) - ord('a')] -= 1   
       start += 1      
       count -= 1     
   print()   

```  

> Template for sliding window (dynamic window) :      
* minStart, minLen can be kept and updated whenever necessary and returned finally     

```   
map = {}  # for hashmaps assisted    
count = 0   
start = 0   
int d; //the length of substring   
for (): initilze hashmap     
// Move end to find a valid window.
for end in range(len(s)):     
    // If char in s exists in t, decrease counter
    if (map[s[end]] > 0) {modify counter here }            
    // Decrease m[s[end]]. If char does not exist in t, m[s[end]] will be negative.       
		m[s[end]]--       
      end++         
      // When we found a valid window, move start to find smaller window.     
    while(counter condition){                 
          
          if (end - start < minLen or any other condition)
          {update d here if finding minimum }

          increase begin to make it invalid/valid again         
                
          m[s[start]]++    
          // When char exists in t, increase counter.   
            if (m[s[start]] > 0)    
          { modify counter here }                  
            } 
           start++        
    
    update d here if finding maximum        
 
return d / return s.substr(minStart, minLen);       
```                 

> Template for sliding window + deque based approach :  

// store the indices not the element in the deque    
// process first k elements in the deque   

```    
Deque = deque()
for i in range(k):
    // conditions for adding to deque 	
```   
// Now, process remaining elements    

```    
for i in range(k, n):
    // print the front of deque as answer (add conditions if necessary)
    print(Deque[0])   
    // remove the non useful elements from the current window 
    while Deque and Deque[0] <= i - k:
        Deque.popleft()
    
    // add conditions for adding/appending elements to the deque 

// finally, add the answer for the last window also print(Deque[0])
```   

