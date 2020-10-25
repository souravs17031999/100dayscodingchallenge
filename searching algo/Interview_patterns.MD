# Common Interview Patterns :    
*  Apply binary search : Look for monotonic sequences like strictly increasing or decreasing / sorted order.      
*  Look for exact range (maybe infinite), find start value and end value.   
*  If it looks like sorted series like start = 10, end = 30, and we can try every possible value from 10...11...12...13.........30, then we need to apply binary  
search to optimize it as this series is itself sorted. This is also called modified binary search pattern.   
* That means it's not necessary that array will be given, we need to explicitly, find range in which our answer can lie and then find if sequence is sorted from start....end.  
* Sometimes, the given array will not be sorted but then also, we can apply modified binary search using concept of "promising search space", that means find some criterior which
can reduce the search space to either half side by proving any one of the side is can give promising answer in that range meaning we don;t know exaclty, but with some conditions, 
we are having probability of finding the answer in that half space.   
