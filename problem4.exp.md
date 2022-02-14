# Idea 

Solved this problem using a two pointer kind of approach. 
I used Three Pointers in total, 

1. Zero Pointer --> One that gives the swappable position for the zero (0) elements
2. Two (2) Pointer --> One that gives the swappable position for the two (2) elements 
3. Current Pointer to traverse the array  

When the current pointer encounters a "0" element I swap it with the element present at the zero pointer and continue traversing from that position without incrementing.


When the current pointer encounters a "2" element I swap it with the element present at the zero pointer and continue traversing from that position without incrementing. 

When the current pointer encounters "1" we increment the current pointer. 

Time Complexity: O(n) 
Space Complexity: O(1)