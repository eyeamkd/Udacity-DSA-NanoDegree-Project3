# Quick Sort

## Important things to keep in mind:

- This algorithm is more counter intuitive, which means that, if pivot element that was picked is the element that is actually placed where it belongs, for example the biggest element or the second biggest element, then all the comparisions that follow are useless which simulates bubble sort, and hence
O(n*n) time complexity


# Algorithm:

- Pick a pivot element
- Compare the pivot element and replace the element into categories of "higher than pivot", "lower than pivot"
- The above steps should result into two halves, with the pivot element being in the center
- Repeat the step with the two halves, having their respective pivots, the end result of recursion would be a sorted array 


