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
# We keep a simple ARRAY,  
