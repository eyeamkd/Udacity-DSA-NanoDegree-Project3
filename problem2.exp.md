# Idea:

The idea that I came up to solve this problem was to use binary search two times, as the effective time complexity of the solution would still remain O(logn)

as O(K*logn) ~= O(logn)
i.e Binary search no matter how many times used, the effective time complexity of the algorithm is still O(logn)

Therefore, I have written two types of Binary Search functions, one that searches for the pivot element and the other one that divides the array using the pivot and searches for the value

Space Complexity: O(1)
since no extra data structure is used 
Time Complexity: O(logn)