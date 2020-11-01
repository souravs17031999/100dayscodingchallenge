# Program to design a hit counter.
# It should support the following two operations: hit and getHits.
#
# hit(timestamp) – Shows a hit at the given timestamp.
# getHits(timestamp) – Returns the number of hits received in the past 5 minutes (300 seconds) (from currentTimestamp).
# ASSUMPTIONS : 
# Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order 
# (i.e. the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.
#
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# Examples:
#
#
# HitCounter counter = new HitCounter();
#
# // hit at timestamp 1.
# counter.hit(1);
#
# // hit at timestamp 2.
# counter.hit(2);
#
# // hit at timestamp 3.
# counter.hit(3);
#
# // get hits at timestamp 4, should return 3.
# counter.getHits(4);
#
# // hit at timestamp 300.
# counter.hit(300);
#
# // get hits at timestamp 300, should return 4.
# counter.getHits(300);
#
# // get hits at timestamp 301, should return 3.
# counter.getHits(301);
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# FIRST APPROACH : 
# We keep a simple ARRAY, more precisely resiazble array - vector (list), to fill the timestamps as they come in, and then for getting last 5min or 300 seconds, we subtract
# current timestamp from 300 to get range/duration, now keep moving the index from front till we get inside range.

class HitCounter:
    
    def __init__(self):
        self.arr = [] # too much space 
        self.size = 0
    
    # time : 0(1), space : 0(1)
    def hit(self, timestamp):
        self.arr.append(timestamp)
        self.size += 1
    
    # time : 0(N), space : 0(1)
    def get_hits(self, timestamp):
        idx = 0
        while idx >= 0 and self.arr[idx] <= timestamp - 300:
            idx += 1
        
        return self.size - idx

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# SECOND APPROACH : 
# Also, now we can observe that too much space is wasted in above solution, because we are keeping non useful elements also in array.
# we need to remove these non useful array elements.
# So, we go for queue based approach : 
# Now, in queue, we keep only useful elements, and pop out all non useful elements.

from collections import deque
class HitCounter:
    
    def __init__(self):
        self.queue = deque() # little space efficient than above approach
        self.size = 0
    
    # time : 0(1), space : 0(1)
    def hit(self, timestamp):
        self.queue.append(timestamp)
        self.size += 1
    
    # time : 0(N), space : 0(1)
    def get_hits(self, timestamp):
        while self.queue and timestamp - self.queue[0] >= 300:
            self.queue.popleft()
            self.size -= 1
        
        return self.size
      
# Can we do more better ?
# We maintain two arrays of 300 size, counter and time.
# time basically stores timestamps when we call hit() and counter stores how many this index timestamp is called.
# so, if it is called two times, then we can increment directly the value of counter at this index.
# When, get_hits() is called, then we can simply iterate over complete time array of 300 indices, because timestamps are distirbuted randomly, so, we have to check all of them
# but it is constant, check for if timstamp comes under range of 300, then simply keep running sum from counter value at this index.
# --------------------------------------------------------------------------------------------------------------------------------------------

class HitCounter:
    
    def __init__(self):
        self.counter = [0] * 300
        self.time = [0] * 300
    
    # time : 0(1), space : 0(1)
    def hit(self, timestamp):
        idx = timestamp % 300
        if self.time[idx] != timestamp:
            self.time[idx] = timestamp
            self.counter[idx] = 1
        else:
            self.counter[idx] += 1
    
    # time : 0(1), space : 0(1)
    def get_hits(self, timestamp):
        res = 0
        for i in range(300):
            if timestamp - self.time[i] < 300:
                res += self.counter[i]
        
        return res
      
 
# More ideas can be applied for distributed systems, locks etc...
