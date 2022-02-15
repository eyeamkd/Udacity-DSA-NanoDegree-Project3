# Idea 
This problem was pretty straight forward and helped me to know the implementation of Trie in real life use cases 

I built each node of the Trie, to have the letter and the end result if it's a word or not, also a children={} property to contain the nodes below it 

With each letter that typed into the text box, the function traverses through the children of the node containing the sequence in the input box and returns all the results ( node that have end result as true) 

The above approach is quite costly ( atleast seems to be), and it depends on the depth and children of the of the Trie, hence a Time Complexity is O(N*D) where there are 'N' elements with 'D' depth each.
I think it's because of this massive complexity that services like Algolia Search don't display the results until unless atleast 3-4 characters are typed. Which decreases the possible chances by "D" times.

The Space Complexity is O(S*C), where 'C' is the number of unique character present and S is the space required by each node.