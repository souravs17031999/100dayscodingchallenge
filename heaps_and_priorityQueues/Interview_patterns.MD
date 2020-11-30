# Important trick for Heaps/Priority queues :   
* Try to build heap from array/list if all the elements are known beforehand   
which will be going inside heaps as it will take linear time 0(N) otherwise   
going for one by one would take 0(N*log(N)) and it's inefficient.   
* Convert elements into tuples by using :       
```[() for _ .....]``` and then pass into heapify directly.   

* More examples (Priority queues):       
> Let's say we have hashmaps using Counter/ dict      
```count = dict()/Counter()```     
```ele = [(count.get(i), i) for _ in count]```   
```heapify(ele)```        
> Let's say we used array for hashmaps   
```count = [2, 1, 3, 4, 0, 0, 1, 0, 0, 1]```    
```ele = [(count[i], i) for i in range(len(count)) if count[i]]```    
```heapify(ele)```    
> For max heaps (upper was using min heaps):       
```ele = [-(count[i], i) for i in range(len(count)) if count[i]]```    
```heapify(ele)```
```    
* If using Priority Queue and update is required in value, since there is no function for "increase_key" operation,
* so, we need to know exact index at which the elements is so that we can change that index value.
* We Should use hashmaps for mapping the index to the elements and keep updating it in any operation (helpful for increase_key) 
